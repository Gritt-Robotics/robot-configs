"""
List the robots a range of commits affects, with the release each is assigned.

A robot is affected when its robot tree or its assignment changed, when the fleet it is
assigned to changed, or when CI or checkout settings changed. Robots with no assignment at the
head commit are left out. The release image's validator checks assignments in full; this reads
only the two fields CI routes on.

Usage (from the repo root):
    python3 ci/affected_robots.py (--base <commit> | --all) [--head <commit>] [--by-release]
Prints `<robot> <release>` per line, or `<release> <robot>...` per line with --by-release.
"""

import argparse
import re
import subprocess
import sys
from collections.abc import Iterable

ROBOTS_DIR = "robots"
FLEETS_DIR = "fleets"
ASSIGNMENTS_DIR = "assignments"
ASSIGNMENT_SUFFIX = ".yaml"
# A change under these paths can change what any robot validates or checks out.
GLOBAL_PATHS = ("ci", ".github", ".gitattributes")
FLEET_KEY = "fleet"
RELEASE_KEY = "release"
NAME_PATTERN = re.compile(r"^[a-z0-9_]+$")
RELEASE_PATTERN = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+$")
QUOTES = "\"'"


class AssignmentError(ValueError):
    """An assignment file lacks a fleet or release CI can route on."""


def parse_assignment(robot: str, text: str) -> tuple[str, str]:
    """
    Read the fleet and release from an assignment file's YAML mapping of plain scalars.

    Args:
        robot (str): The robot the assignment belongs to, for error messages.
        text (str): The assignment file's contents.

    Returns:
        tuple[str, str]: The robot's fleet and release tag.

    Raises:
        AssignmentError: If the fleet or release is missing, repeated or malformed.
    """
    values = {}
    for line in text.splitlines():
        content = line.split("#", 1)[0].strip()
        if content == "":
            continue
        key, separator, value = content.partition(":")
        key = key.strip()
        if separator == "" or key in values:
            raise AssignmentError(f"{robot}: unexpected line {line!r}")
        values[key] = value.strip().strip(QUOTES)
    fleet = values.get(FLEET_KEY, "")
    release = values.get(RELEASE_KEY, "")
    if NAME_PATTERN.fullmatch(fleet) is None:
        raise AssignmentError(f"{robot}: fleet {fleet!r} is not a fleet name")
    if RELEASE_PATTERN.fullmatch(release) is None:
        raise AssignmentError(f"{robot}: release {release!r} is not a vX.Y.Z tag")
    return fleet, release


def affected_robots(
    changed_paths: Iterable[str] | None, assignments: dict[str, tuple[str, str]]
) -> dict[str, str]:
    """
    Select the assigned robots a set of changed paths affects.

    Args:
        changed_paths (Iterable[str] | None): Repo-relative changed paths; None for every robot.
        assignments (dict[str, tuple[str, str]]): Each assigned robot's fleet and release.

    Returns:
        dict[str, str]: Each affected robot's release, sorted by robot.
    """
    if changed_paths is None:
        robots = set(assignments)
    else:
        robots = set()
        for path in changed_paths:
            parts = path.split("/")
            if parts[0] in GLOBAL_PATHS:
                robots = set(assignments)
                break
            if parts[0] == ROBOTS_DIR and len(parts) > 2:
                robots.add(parts[1])
            elif parts[0] == ASSIGNMENTS_DIR and len(parts) == 2:
                robots.add(parts[1].removesuffix(ASSIGNMENT_SUFFIX))
            elif parts[0] == FLEETS_DIR and len(parts) > 2:
                robots |= {
                    robot
                    for robot, (fleet, _) in assignments.items()
                    if fleet == parts[1]
                }
    return {
        robot: assignments[robot][1] for robot in sorted(robots) if robot in assignments
    }


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


def _assignments_at(commit: str) -> dict[str, tuple[str, str]]:
    assignments = {}
    for path in _git("ls-tree", "--name-only", f"{commit}:{ASSIGNMENTS_DIR}").split():
        if not path.endswith(ASSIGNMENT_SUFFIX):
            continue
        robot = path.removesuffix(ASSIGNMENT_SUFFIX)
        if NAME_PATTERN.fullmatch(robot) is None:
            raise AssignmentError(f"{path}: {robot!r} is not a robot name")
        assignments[robot] = parse_assignment(
            robot, _git("show", f"{commit}:{ASSIGNMENTS_DIR}/{path}")
        )
    return assignments


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    since = parser.add_mutually_exclusive_group(required=True)
    since.add_argument("--base", help="the commit the changes are measured from")
    since.add_argument("--all", action="store_true", help="every assigned robot")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--by-release", action="store_true")
    args = parser.parse_args()

    changed = (
        None
        if args.all
        else _git("diff", "--name-only", args.base, args.head).splitlines()
    )
    try:
        robots = affected_robots(changed, _assignments_at(args.head))
    except AssignmentError as error:
        sys.exit(f"error: {error}")
    if not args.by_release:
        for robot, release in robots.items():
            print(f"{robot} {release}")
        return
    by_release = {}
    for robot, release in robots.items():
        by_release.setdefault(release, []).append(robot)
    for release, names in sorted(by_release.items()):
        print(release, *names)


if __name__ == "__main__":
    main()
