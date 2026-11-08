#!/bin/bash
# usage: fetch_hedra.sh OUTDIR ACCESS_KEY_ID TOKEN_FILE  < lines "beat uuid signature expires"
# Rebuilds Hedra presigned S3 URLs (shared key id + token, per-file signature) and downloads beat_XX.mp3
OUT=$1; KID=$2; TOK=$(cat "$3")
BASE="https://hedra-api-audio-6923ef8dbda63b10.s3.amazonaws.com/web-app-v2/audio/14b61fb9-30c0-5eee-8ca9-e791c3ecc212"
while read -r b u s e; do
  [ -z "$b" ] && continue
  curl -sS -o "$OUT/beat_$b.mp3" -w "beat_$b %{http_code} %{size_download}\n" \
    "$BASE/$u.mp3?response-content-type=audio%2Fmpeg&AWSAccessKeyId=$KID&Signature=$s&x-amz-security-token=$TOK&Expires=$e"
done
