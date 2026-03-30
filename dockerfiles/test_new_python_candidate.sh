# This script is meant for development, which produces fresh images and then runs tests
# If it succeeds, a new python version can be added to CI
# Run via
# sh dockerfiles/test_new_python_candidate.sh

# Stop on error https://stackoverflow.com/a/2871034/10882657
set -e

# Set which versions to use
export VERSION_NUMBER=${VERSION_NUMBER:-0.9.9}
export PYTHON_VERSION=${PYTHON_VERSION:-3.14}
export SC2_VERSION=${SC2_VERSION:-4.10}

# For better readability, set local variables
IMAGE_NAME=burnysc2/python-sc2-docker:py_$PYTHON_VERSION-sc2_$SC2_VERSION-v$VERSION_NUMBER
BUILD_ARGS="--build-arg PYTHON_VERSION=$PYTHON_VERSION --build-arg SC2_VERSION=$SC2_VERSION"

# Build image
docker build -f dockerfiles/Dockerfile -t $IMAGE_NAME $BUILD_ARGS .

# Delete previous container if it exists
docker rm -f test_container

# Start container
# https://docs.docker.com/storage/bind-mounts/#use-a-read-only-bind-mount
docker run -i -d \
  --name test_container \
  --env 'PYTHONPATH=/root/python-sc2' \
  --entrypoint /bin/bash \
  $IMAGE_NAME

# Install requirements
docker exec -i test_container mkdir -p /root/python-sc2
docker cp pyproject.toml test_container:/root/python-sc2/
docker cp uv.lock test_container:/root/python-sc2/
docker exec -i test_container bash -c "pip install uv && cd python-sc2 && uv sync --no-cache --no-install-project"

docker cp sc2 test_container:/root/python-sc2/sc2
docker cp test test_container:/root/python-sc2/test

# Run various test bots
docker exec -i test_container bash -c "cd python-sc2 && uv run python test/travis_test_script.py test/autotest_bot.py"

docker cp examples test_container:/root/python-sc2/examples
docker exec -i test_container bash -c "cd python-sc2 && uv run python test/run_example_bots_vs_computer.py"
