#!/usr/bin/env bash

echo "Checking for ThinkPad OS updates..."

cd "$HOME/thinkpad-os" || exit 1

LOCAL_VERSION=$(cat VERSION | tr -d '[:space:]')
LATEST_VERSION=$(curl -s https://raw.githubusercontent.com/Aector84/thinkpad-os/main/VERSION | tr -d '[:space:]')

if [ -z "$LATEST_VERSION" ]; then
    echo "Could not retrieve latest version."
    exit 1
fi

if [ "$LOCAL_VERSION" = "$LATEST_VERSION" ]; then
    echo "Already up to date. Version $LOCAL_VERSION"
    exit 0
fi

echo "Updating from $LOCAL_VERSION to $LATEST_VERSION..."

git pull
./install.sh

echo "$LATEST_VERSION" > VERSION

echo "Update complete. Now running version $LATEST_VERSION"
