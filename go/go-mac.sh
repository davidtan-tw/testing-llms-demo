#!/bin/sh

set -e

echo "Installing homebrew if it's not installed..."
which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Prevent homebrew from running brew update --auto-update when running brew install, which can take quite long if user has many outdated packages
export HOMEBREW_NO_AUTO_UPDATE=1

echo "Installing Python 3 if it's not installed..."
which python3 || brew install python3

echo "Installing dependencies on host (so that we can configure a virtual environment for our IDE)"
./scripts/go/install-dependencies-on-host.sh
