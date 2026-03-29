# Set up StarCraft II Test Environment for python-sc2 bots (not pysc2 bots!)
ARG PYTHON_VERSION=3.10

# https://docs.astral.sh/uv/guides/integration/docker/#available-images
FROM ghcr.io/astral-sh/uv:python$PYTHON_VERSION-bookworm-slim AS base

ARG SC2_VERSION=4.10

# Debugging purposes
RUN echo $PYTHON_VERSION
RUN echo $SC2_VERSION

USER root

# Update system
RUN apt-get update \
    && apt-get upgrade --assume-yes --quiet=2

# Update and install packages for SC2 development environment
# gcc to compile packages
# libc6-dev required by gcc: /usr/local/include/python3.12/Python.h:23:12: fatal error: stdlib.h: No such file or directory
# git, unzip and wget for download and extraction
# rename to rename maps
# tree for debugging
RUN apt-get install --assume-yes --no-install-recommends --no-show-upgraded \
    gcc \
    libc6-dev \
    git  \
    unzip \
    curl \
    rename \
    tree

# Set working directory to root, this uncompresses StarCraftII below to folder /root/StarCraftII
WORKDIR /root/

# Download and uncompress StarCraftII from https://github.com/Blizzard/s2client-proto#linux-packages and remove zip file
# If file is locally available, use this instead:
#COPY SC2.4.10.zip /root/
RUN curl --retry 5 --retry-delay 5 -C - http://blzdistsc2-a.akamaihd.net/Linux/SC2.$SC2_VERSION.zip -o "SC2.$SC2_VERSION.zip" \
    && unzip -q -P iagreetotheeula "SC2.$SC2_VERSION.zip" \
    && rm SC2.$SC2_VERSION.zip

# Remove Battle.net folder
RUN rm -rf /root/StarCraftII/Battle.net/* \
    # Remove Shaders folder
    && rm -rf /root/StarCraftII/Versions/Shaders*

# Create a symlink for the maps directory
RUN ln -s /root/StarCraftII/Maps /root/StarCraftII/maps \
    # Remove the Maps that come with the SC2 client
    && rm -rf /root/StarCraftII/maps/*

# See download_maps.sh
COPY dockerfiles/maps/* /root/StarCraftII/maps/

# Squash image with trick https://stackoverflow.com/a/56118557/10882657
FROM scratch
COPY --from=base / /
WORKDIR /root/
ENTRYPOINT [ "/bin/bash" ]

# To run a python-sc2 bot:
# Install python-sc2 and requirements via pip:
# pip install --upgrade https://github.com/BurnySc2/python-sc2/archive/develop.zip

# To run an example bot, copy one to your container and then run it with python:
# python /your-bot.py