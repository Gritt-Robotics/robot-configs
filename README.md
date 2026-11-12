# robot-configs

The only source of robot and fleet config. A change is a pull request: CI validates every robot
it affects against the code that robot runs, and merging creates a GitHub deployment for each of
those robots. Each robot's agent fetches the config, validates it against the robot's own build,
and activates it. gritt also tracks this repo as a submodule, which the dev container reads
config from.

Design: [Robot Release & Config Deployment Design](https://claude.ai/artifact/TWRbv5mGGX1K6Agw6M554C).

## Layout

| Path | Holds |
| --- | --- |
| `robots/<robot>/` | Everything one robot's stack reads, complete on its own: `robot_manifest.yaml` (its own entry), `cpu_affinity.yaml`, `adapter/`, `perception/` (`zed.json`, lidars, node configs), `planning/`, `control/`, `drs/`, `telemetry/`, `gnss/` (robots with GNSS), `data_collection/`, `calibration_setup/`, `reachability_tolerance_limits.yaml`, `planner_offset_limits.yaml`. The release validates that a robot holds exactly the files it reads. |
| `fleets/<fleet>/` | What a group of robots shares: `object_models.yaml`, `install_direction*.yaml`, `tracker_gap.yaml` |
| `assignments/<robot>.yaml` | The robot's `fleet`, and its `release` (a `vX.Y.Z` image tag) once it runs release images. A robot with no `release` runs a dev container on its own gritt checkout. |
| `ci/` | The helpers the workflows run |

The schemas live in the gritt monorepo and ship in each release image, so a robot is checked by
the schemas it runs.

Not here: robot-local state (operator modes, planner offsets, generated calibrations). It stays
on the robot, in `local/`, and survives every deployment.

## Making a change

Edit the files and open a PR. CI (`validate.yml`) then:
1. works out the affected robots: those whose robot tree or assignment changed, every robot
   assigned to a changed fleet, or every robot when `ci/`, `.github/` or `.gitattributes` changed;
2. validates them with `python3 -m config.validate_bundle repo . --robot ...`:
   - robots with no release, against the config package of gritt `main` (repository variable
     `GRITT_REF` overrides the ref). This runs the file and tree layers only; the robot's agent
     runs every layer against the robot's own build before it activates anything;
   - robots with a release, with `--release` inside `gritt-release:<release>` from Artifact
     Registry.

Moving a robot to another fleet or release is a one-line change to its assignment. The release
must already be published.

On merge, `deploy.yml` creates a deployment for each affected robot: environment `<robot>`, ref
the merge commit, payload `{"release": "<tag>"}` (`checkout` for a robot with no release). The
repo's Environments page shows which commit each robot runs and its history.

## CI requirements

| Workflow | Runs on | Needs |
| --- | --- | --- |
| `validate.yml`, robots with no release | GitHub-hosted | Secret `GRITT_READ_TOKEN`: a fine-grained token that reads `Gritt-Robotics/gritt` contents |
| `validate.yml`, robots with a release | the org's self-hosted runners | Docker, and the runner's GCS reader credential at `~/.config/gritt/gcs/adc.json`, to pull release images. The org's runners must be allowed to run this public repo's jobs. |
| `deploy.yml` | GitHub-hosted | Only the workflow's own token (`deployments: write`) |

Make `Validate` a required check on `main`.

Run the helpers' tests with `python3 -m unittest discover -s ci`.
