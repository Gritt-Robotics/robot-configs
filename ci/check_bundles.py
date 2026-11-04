"""
Check robot-configs bundles: layout, all validation layers, and lineage against a base commit.

Runs inside the Gritt image with the pinned gritt checkout's config package installed.

Usage:
    python3 ci/check_bundles.py [--base <git-ref>] [bundle_dir ...]

With no bundle dirs, checks every bundle. With --base, also checks each bundle replaces the
revision that ref holds.
"""

import argparse
import pathlib
import subprocess
import sys
import tempfile

from config.bundle_manifest import BundleKind, load_manifest
from config.publish_bundle import check_lineage
from config.validate_bundle import (
    load_release_context,
    validate_bundle,
    validate_bundle_against_release,
)

KIND_DIRS = {"robots": BundleKind.ROBOT, "deployments": BundleKind.DEPLOYMENT}


def all_bundles() -> list[pathlib.Path]:
    return sorted(
        path for kind_dir in KIND_DIRS for path in pathlib.Path(kind_dir).iterdir()
    )


def base_bundle(base: str, bundle_dir: pathlib.Path, scratch: pathlib.Path):
    listed = subprocess.run(
        ["git", "ls-tree", "--name-only", base, f"{bundle_dir.as_posix()}/"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    if listed.strip() == "":
        return None
    archive = subprocess.run(
        ["git", "archive", base, bundle_dir.as_posix()], capture_output=True, check=True
    ).stdout
    subprocess.run(["tar", "-x", "-C", str(scratch)], input=archive, check=True)
    return load_manifest(scratch / bundle_dir)


def check(bundle_dir: pathlib.Path, release, base: str | None, scratch) -> None:
    kind_dir, name = bundle_dir.parts[-2], bundle_dir.parts[-1]
    manifest = validate_bundle(bundle_dir)
    if (manifest.kind, manifest.name) != (KIND_DIRS.get(kind_dir), name):
        raise ValueError(
            f"{bundle_dir} holds {manifest.kind.value} bundle {manifest.name!r}:"
            f" it belongs in {next(d for d, k in KIND_DIRS.items() if k == manifest.kind)}/"
            f"{manifest.name}"
        )
    validate_bundle_against_release(bundle_dir, manifest, release)
    if base is not None:
        check_lineage(manifest, base_bundle(base, bundle_dir, scratch))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--base")
    parser.add_argument("bundle_dirs", type=pathlib.Path, nargs="*")
    args = parser.parse_args()
    release = load_release_context()
    failed = False
    with tempfile.TemporaryDirectory() as scratch:
        for bundle_dir in args.bundle_dirs or all_bundles():
            if not bundle_dir.is_dir():
                print(f"deleted: {bundle_dir} (no check)")
                continue
            try:
                check(bundle_dir, release, args.base, pathlib.Path(scratch))
                print(f"ok: {bundle_dir}")
            except ValueError as error:
                print(f"FAILED: {bundle_dir}: {error}")
                failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
