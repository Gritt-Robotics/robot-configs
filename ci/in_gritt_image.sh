#!/usr/bin/env bash
# Run a command in the Gritt image, with the pinned gritt checkout's validation packages built.
# Usage: ci/in_gritt_image.sh <command...>   (from the repo root; expects ./gritt checked out)
set -euo pipefail

IMAGE="${GRITT_IMAGE:-ghcr.io/gritt-robotics/gritt:v16}"
PACKAGES="config sensor_configs sensor_calibration perception_config"
CRED_DIR="${GRITT_PUBLISH_GCS_CRED_DIR:-}"

cred_args=()
if [ -n "$CRED_DIR" ]; then
  cred_args=(-v "$CRED_DIR:/gcs:ro" -e GOOGLE_APPLICATION_CREDENTIALS=/gcs/adc.json)
fi

docker run --rm "${cred_args[@]}" \
  -v "$PWD:/robot-configs" -w /robot-configs \
  "$IMAGE" bash -c "
    set -euo pipefail
    source /opt/ros/jazzy/setup.bash
    colcon --log-base /tmp/log build --base-paths gritt/ros2_ws/src \
      --build-base /tmp/build --install-base /tmp/install \
      --packages-up-to $PACKAGES --cmake-args -DBUILD_TESTING=OFF > /tmp/build.log 2>&1 \
      || { tail -50 /tmp/build.log; exit 1; }
    source /tmp/install/setup.bash
    git config --global --add safe.directory /robot-configs
    $*
  "
