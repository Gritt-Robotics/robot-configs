# robot-configs

The reviewed source of every robot and deployment config bundle. CI validates each PR against
the release robots run, and publishes each merged revision to
`gs://gritt-deployments/test/{robot-configs,deployment-configs}/<name>/revisions/<rev>/`.
Robots never read this repo. They pull published revisions over WireGuard.

## Layout

| Path | Holds |
| --- | --- |
| `robots/<robot>/` | One robot's bundle: `zed.json`, `reachability_tolerance_limits.yaml`, `planner_offset_limits.yaml`, `calibration_setup/`, `calibration/` |
| `deployments/<site>/` | One site's bundle: `object_models.yaml`, `install_direction*.yaml`, `tracker_gap.yaml` |
| `ci/gritt-ref` | The gritt commit whose schemas and release definitions CI validates against |

Each bundle has a `manifest.json` that seals its files. A revision's id is the hash of its
manifest, so the id a PR shows is the id robots run.

Not here:
- Fleet-wide config ships in the release image.
- Robot-local state (planner offsets, operator modes) stays on the robot.

## Changing a bundle

1. Edit the files.
2. Reseal, in the Gritt dev container:
   `python3 -m config.publish_bundle reseal robots/<robot> --author <you>`.
   The new revision records the one it replaces.
3. Open a PR. CI then:
   - runs every validation layer against the pinned release;
   - checks your revision directly replaces the one on `main`. If someone merged first, merge
     `main`, re-apply your edit and reseal.

For a new bundle, add `--kind robot|deployment --name <name>` to the reseal.

Revisions made on a robot (calibration saves, waypoint recordings) come back as automatic PRs
carrying the robot's own manifest. Review and merge them like any other PR.

## CI requirements

Both workflows run on the org's self-hosted runners in `ghcr.io/gritt-robotics/gritt:v16`.

| Workflow | Needs |
| --- | --- |
| `validate.yml` | Secret `ORG_ACCESS_TOKEN_FOR_CI`, to check out gritt |
| `publish.yml` | The same secret, plus a GCS credential that can write `gs://gritt-deployments`, at `~/.config/gritt/gcs-publish/adc.json` on the runner |

Until release images exist, `ci/gritt-ref` pins a gritt commit. Bump it alongside each release.
