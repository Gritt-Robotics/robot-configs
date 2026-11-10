#!/usr/bin/env bash
# Validate each affected robot in the image of its assigned release: the schemas it will run.
# Usage: ci/validate_affected.sh <base-commit>   (from the repo root, logged in to the registry)
set -euo pipefail
shopt -s inherit_errexit

REGISTRY="${GRITT_RELEASE_REGISTRY:-us-docker.pkg.dev/gen-lang-client-0737381909/gritt}"
BASE="${1:?usage: ci/validate_affected.sh <base-commit>}"

groups="$(python3 ci/affected_robots.py --base "$BASE" --by-release)"
if [ -z "$groups" ]; then
    echo "No robot affected."
    exit 0
fi

status=0
while read -r release robots; do
    image="${REGISTRY}/gritt-release:${release}"
    args=()
    for robot in $robots; do
        args+=(--robot "$robot")
    done
    echo "::group::${release}: ${robots}"
    if docker pull --quiet "$image" \
        && docker run --rm --network none -v "$PWD:/config-repo:ro" "$image" \
            python3 -m config.validate_bundle repo /config-repo "${args[@]}" --release; then
        echo "${release}: valid"
    else
        echo "::error::${release}: ${robots} failed validation (or the image is missing)"
        status=1
    fi
    echo "::endgroup::"
done <<< "$groups"
exit "$status"
