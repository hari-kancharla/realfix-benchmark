# RealFix Pilot v1 hermetic test image: realfix-pilot:2
# Carries no harness source and no benchmark/upstream source. Each case bind-mounts its
# materialized tree at /workspace and runs with --network none. PYTHONPATH=/workspace/src
# makes src-layout packages (e.g. src/packaging, src/click, src/attr) importable from the
# materialized source; flat-layout packages (more_itertools, rich, idna) import from the
# working directory.
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/workspace/src

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /workspace
