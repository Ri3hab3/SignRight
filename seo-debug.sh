#!/usr/bin/env bash
SITE="${1:-https://signright.io}"
SITEMAP="$SITE/sitemap.xml"

printf "%-55s | %-4s | %-8s | %-6s | %-5s | %s\n" "URL" "HTTP" "X-ROBOTS" "META" "WORDS" "CANONICAL"
printf '%.0s-' {1..150}; echo

curl -s "$SITEMAP" \
  | grep -oE '<loc>[^<]+</loc>' \
  | sed -E 's|</?loc>||g' \
  | while read -r url; do

  hdr=$(curl -sI -L "$url")
  code=$(echo "$hdr" | grep -iE '^HTTP/' | tail -1 | awk '{print $2}')
  xrob=$(echo "$hdr" | grep -i 'x-robots-tag' | sed 's/.*: //' | tr -d '\r' | head -1)
  [ -z "$xrob" ] && xrob="-"

  body=$(curl -s -L "$url")

  meta=$(echo "$body" | grep -ioE '<meta[^>]+name=["'"'"']robots["'"'"'][^>]*>' \
         | grep -ioE 'content=["'"'"'][^"'"'"']+' | sed 's/content=.//' | head -1)
  [ -z "$meta" ] && meta="-"

  canon=$(echo "$body" | grep -ioE '<link[^>]+rel=["'"'"']canonical["'"'"'][^>]*>' \
          | grep -ioE 'href=["'"'"'][^"'"'"']+' | sed 's/href=.//' | head -1)
  [ -z "$canon" ] && canon="!! MISSING !!"

  words=$(echo "$body" \
    | sed -E 's|<script[^>]*>.*</script>||gI; s|<style[^>]*>.*</style>||gI' \
    | sed -E 's/<[^>]+>/ /g' | tr -s '[:space:]' ' ' | wc -w | tr -d ' ')

  short="${url:0:55}"
  printf "%-55s | %-4s | %-8s | %-6s | %-5s | %s\n" "$short" "$code" "$xrob" "$meta" "$words" "$canon"
done
