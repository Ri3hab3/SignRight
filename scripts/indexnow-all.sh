#!/usr/bin/env bash
# Submit EVERY URL in sitemap.xml to IndexNow (Bing, Yandex, Seznam, Naver).
# Run this AFTER a deploy is live on https://signright.io — IndexNow verifies
# the key file over HTTP before it accepts the batch. Google ignores IndexNow,
# so still use Search Console "Request indexing" for Google.
#
#   ./scripts/indexnow-all.sh
#
set -euo pipefail
cd "$(dirname "$0")/.."

HOST="signright.io"
KEY="446fe6c13f3fa79da08df6c24d92307a"
KEY_LOCATION="https://$HOST/$KEY.txt"

echo "Checking the key file is reachable…"
if ! curl -fsS "$KEY_LOCATION" >/dev/null; then
  echo "ERROR: $KEY_LOCATION is not reachable. Deploy first, then re-run." >&2
  exit 1
fi

# Pull every <loc> out of the sitemap.
mapfile -t URLS < <(grep -oE '<loc>[^<]+</loc>' sitemap.xml | sed -E 's#</?loc>##g')
if [ "${#URLS[@]}" -eq 0 ]; then
  echo "ERROR: no URLs found in sitemap.xml" >&2; exit 1
fi
echo "Found ${#URLS[@]} URLs in sitemap.xml"

payload=$(python3 - "$HOST" "$KEY" "$KEY_LOCATION" "${URLS[@]}" <<'PY'
import json, sys
host, key, loc, *urls = sys.argv[1:]
print(json.dumps({"host": host, "key": key, "keyLocation": loc, "urlList": urls}))
PY
)

echo "Submitting ${#URLS[@]} URLs to IndexNow…"
code=$(curl -sS -o /tmp/indexnow-response.txt -w '%{http_code}' \
  -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data "$payload")

echo "HTTP $code"; cat /tmp/indexnow-response.txt; echo
case "$code" in
  200|202) echo "✓ Accepted. Indexing is queued — not instant." ;;
  400) echo "✗ Bad request (payload)." >&2; exit 1 ;;
  403) echo "✗ Key rejected: $KEY_LOCATION must return exactly the key." >&2; exit 1 ;;
  422) echo "✗ URL/host or key mismatch." >&2; exit 1 ;;
  429) echo "✗ Rate limited. Wait and retry." >&2; exit 1 ;;
  *)   echo "✗ Unexpected response." >&2; exit 1 ;;
esac
