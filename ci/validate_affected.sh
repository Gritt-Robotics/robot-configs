#!/usr/bin/env bash
# Validate each affected robot against the code it will run; README.md says how per mode.
# Usage: ci/validate_affected.sh <base-commit> (checkout <gritt-checkout> | release)
set -euo pipefail
shopt -s inherit_errexit

REGISTRY="${GRITT_RELEASE_REGISTRY:-us-docker.pkg.dev/gen-lang-client-0737381909/gritt}"
CHECKOUT=checkout
USAGE="usage: ci/validate_affected.sh <base-commit> (checkout <gritt-checkout> | release)"
BASE="${1:?$USAGE}"
MODE="${2:?$USAGE}"
case "$MODE" in
    "$CHECKOUT") GRITT="${3:?$USAGE}" ;;
    release) ;;
    *) echo "$USAGE" >&2; exit 2 ;;
esac

groups="$(python3 ci/affected_robots.py --base "$BASE" --by-release)"
if [ -z "$groups" ]; then
    echo "No robot affected."
    exit 0
fi

status=0
while read -r release robots; do
    # Each mode checks only its own robots; the other job checks the rest.
    if { [ "$MODE" = "$CHECKOUT" ] && [ "$release" != "$CHECKOUT" ]; } \
        || { [ "$MODE" = release ] && [ "$release" = "$CHECKOUT" ]; }; then
        continue
    fi
    args=()
    for robot in $robots; do
        args+=(--robot "$robot")
    done
    echo "::group::${release}: ${robots}"
    if [ "$release" = "$CHECKOUT" ]; then
        # Layers 1 and 2 only: the release layer needs a built workspace.
        if PYTHONPATH="$GRITT/ros2_ws/src/config" \
            python3 -m config.validate_bundle repo . "${args[@]}"; then
            echo "${release}: valid"
        else
            echo "::error::${robots} failed validation against gritt's config package"
            status=1
        fi
    else
        image="${REGISTRY}/gritt-release:${release}"
        if docker pull --quiet "$image" \
            && docker run --rm --network none -v "$PWD:/config-repo:ro" "$image" \
                python3 -m config.validate_bundle repo /config-repo "${args[@]}" --release; then
            echo "${release}: valid"
        else
            echo "::error::${release}: ${robots} failed validation (or the image is missing)"
            status=1
        fi
    fi
    echo "::endgroup::"
done <<< "$groups"
exit "$status"
