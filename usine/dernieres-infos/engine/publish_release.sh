#!/bin/bash
# Publish a finished MP4 as a GitHub release asset on the public media repo and print its public URL.
# usage: publish_release.sh FILE.mp4 TAG "Release title"
set -euo pipefail
REPO=TradingFamily10/tf-reels-media
FILE=$1; TAG=$2; TITLE=$3
NAME=$(basename "$FILE")
ID=$(gh api "repos/$REPO/releases" -f tag_name="$TAG" -f name="$TITLE" -f body="Reel Invest Family Fr — usine Dernières Infos" --jq .id)
gh api -X POST "https://uploads.github.com/repos/$REPO/releases/$ID/assets?name=$NAME" \
   -H "Content-Type: video/mp4" --input "$FILE" --jq .browser_download_url
