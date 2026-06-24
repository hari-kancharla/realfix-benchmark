#!/usr/bin/env bash
# Build the RealFix Pilot v1 Batch 1 hermetic test image from the pinned lock.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
docker build --tag realfix-pilot-batch-01:1 "$here"
