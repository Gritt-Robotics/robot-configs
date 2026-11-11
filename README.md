# robot-configs

The only source of robot and fleet config. A change is a pull request: CI validates every robot
it affects against the release that robot runs, and merging creates a GitHub deployment for
each of those robots. Each robot's agent fetches its deployment's commit over WireGuard, stages
it, activates it and reports the result as the deployment's status.

Design: [Robot Release & Config Deployment Design](https://claude.ai/artifact/TWRbv5mGGX1K6Agw6M554C).

## Layout

| Path | Holds |
| --- | --- |
| `robots/<robot>/` | Everything one robot's stack reads, complete on its own: `robot_manifest.yaml` (its own entry), `cpu_affinity.yaml`, `adapter/`, `perception/` (`zed.json`, lidars, node configs), `planning/`, `control/`, `drs/`, `telemetry/`, `gnss/` (robots with GNSS), `data_collection/`, `calibration_setup/`, `reachability_tolerance_limits.yaml`, `planner_offset_limits.yaml`. The release validates that a robot holds exactly the files it reads. |
| `fleets/<fleet>/` | What a group of robots shares: `object_models.yaml`, `install_direction*.yaml`, `tracker_gap.yaml` |
| `assignments/<robot>.yaml` | The robot's `fleet` and `release` (a `vX.Y.Z` image tag) |
| `ci/` | The helpers the workflows run |

The schemas live in the gritt monorepo and ship in each release image, so a robot is checked by
the schemas it runs.

Not here: robot-local state (operator modes, planner offsets, generated calibrations). It stays
on the robot, in `local/`, and survives every deployment.

## Making a change

Edit the files and open a PR. CI (`validate.yml`) then:
1. works out the affected robots: those whose robot tree or assignment changed, every robot
   assigned to a changed fleet, or every robot when `ci/`, `.github/` or `.gitattributes` changed;
2. runs `python3 -m config.validate_bundle repo . --robot ... --release` for each group of them,
   inside `gritt-release:<release>` from Artifact Registry.

Moving a robot to another fleet or release is a one-line change to its assignment. The release
must already be published.

On merge, `deploy.yml` creates a deployment for each affected robot: environment `<robot>`, ref
the merge commit, payload `{"release": "<tag>"}`. The repo's Environments page shows which commit
each robot runs and its history.

## CI requirements

Both workflows run on the org's self-hosted runners.

| Workflow | Needs |
| --- | --- |
| `validate.yml` | Docker, and the runner's GCS reader credential at `~/.config/gritt/gcs/adc.json`, to pull release images |
| `deploy.yml` | Only the workflow's own token (`deployments: write`) |

Make `Validate` a required check on `main`.

Run the helpers' tests with `python3 -m unittest discover -s ci`.
