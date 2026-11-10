"""Tests for affected_robots; run with `python3 -m unittest discover -s ci`."""

import unittest

from affected_robots import AssignmentError, affected_robots, parse_assignment

FLEET = "northwest"
OTHER_FLEET = "southeast"
RELEASE = "v1.0.0"
NEXT_RELEASE = "v1.1.0"
CARAMEL = "caramel"
NACHO = "nacho"
TEST_BENCH = "test_bench"
ASSIGNMENTS = {
    CARAMEL: (FLEET, RELEASE),
    NACHO: (FLEET, NEXT_RELEASE),
    TEST_BENCH: (OTHER_FLEET, RELEASE),
}


class ParseAssignmentTest(unittest.TestCase):
    def test_reads_the_migrated_format(self):
        text = f"fleet: {FLEET}\nrelease: {RELEASE}\n"

        self.assertEqual(parse_assignment(NACHO, text), (FLEET, RELEASE))

    def test_allows_comments_quotes_and_fields_ci_does_not_route_on(self):
        text = f"# moved for the pilot\nfleet: '{FLEET}'\nrelease: \"{RELEASE}\"\nconfig: main\n"

        self.assertEqual(parse_assignment(NACHO, text), (FLEET, RELEASE))

    def test_rejects_a_release_that_is_not_a_tag(self):
        with self.assertRaises(AssignmentError):
            parse_assignment(NACHO, f"fleet: {FLEET}\nrelease: latest\n")

    def test_rejects_a_missing_fleet(self):
        with self.assertRaises(AssignmentError):
            parse_assignment(NACHO, f"release: {RELEASE}\n")

    def test_rejects_a_repeated_key(self):
        with self.assertRaises(AssignmentError):
            parse_assignment(
                NACHO, f"fleet: {FLEET}\nfleet: {OTHER_FLEET}\nrelease: {RELEASE}\n"
            )


class AffectedRobotsTest(unittest.TestCase):
    def test_a_robot_tree_change_affects_only_that_robot(self):
        changed = [f"robots/{NACHO}/perception/zed.json"]

        self.assertEqual(affected_robots(changed, ASSIGNMENTS), {NACHO: NEXT_RELEASE})

    def test_an_assignment_change_affects_that_robot(self):
        changed = [f"assignments/{TEST_BENCH}.yaml"]

        self.assertEqual(affected_robots(changed, ASSIGNMENTS), {TEST_BENCH: RELEASE})

    def test_a_fleet_change_affects_every_robot_assigned_to_it(self):
        changed = [f"fleets/{FLEET}/object_models.yaml"]

        self.assertEqual(
            affected_robots(changed, ASSIGNMENTS),
            {CARAMEL: RELEASE, NACHO: NEXT_RELEASE},
        )

    def test_a_ci_change_affects_every_robot(self):
        self.assertEqual(
            affected_robots(["ci/affected_robots.py"], ASSIGNMENTS),
            {robot: release for robot, (_, release) in ASSIGNMENTS.items()},
        )

    def test_none_selects_every_robot(self):
        self.assertEqual(set(affected_robots(None, ASSIGNMENTS)), set(ASSIGNMENTS))

    def test_a_robot_without_an_assignment_is_left_out(self):
        changed = ["robots/retired/perception/zed.json", "assignments/retired.yaml"]

        self.assertEqual(affected_robots(changed, ASSIGNMENTS), {})

    def test_a_readme_change_affects_no_robot(self):
        self.assertEqual(affected_robots(["README.md", "CODEOWNERS"], ASSIGNMENTS), {})


if __name__ == "__main__":
    unittest.main()
