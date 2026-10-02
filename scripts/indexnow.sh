#!/usr/bin/env bash
# Submit the travel-form URLs to IndexNow (Bing, Yandex, Seznam, Naver).
# Run this AFTER the pages are live on https://signright.io — IndexNow verifies
# the key file over HTTP before it accepts the batch.
#
#   ./scripts/indexnow.sh
#
# Verify the key file first:  curl -s https://signright.io/446fe6c13f3fa79da08df6c24d92307a.txt
set -euo pipefail

HOST="signright.io"
KEY="446fe6c13f3fa79da08df6c24d92307a"
KEY_LOCATION="https://$HOST/$KEY.txt"

URLS=(
  "https://$HOST/travel"
  "https://$HOST/air-suvidha-form"
  "https://$HOST/india-e-arrival-card"
  "https://$HOST/india-arrival-checker"
  "https://$HOST/dubai-to-india-travel-requirements"
  "https://$HOST/hi/air-suvidha-form"
  "https://$HOST/hi/dubai-to-india-travel-requirements"
)

echo "Checking the key file is reachable…"
if ! curl -fsS "$KEY_LOCATION" >/dev/null; then
  echo "ERROR: $KEY_LOCATION is not reachable. Deploy first, then re-run." >&2
  exit 1
fi

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

echo "HTTP $code"
cat /tmp/indexnow-response.txt; echo
case "$code" in
  200|202) echo "✓ Accepted. Indexing is queued — it is not instant." ;;
  400) echo "✗ Bad request: check the JSON payload." >&2; exit 1 ;;
  403) echo "✗ Key rejected: $KEY_LOCATION must return exactly the key." >&2; exit 1 ;;
  422) echo "✗ URLs do not match the host, or the key does not match." >&2; exit 1 ;;
  429) echo "✗ Rate limited. Wait and retry." >&2; exit 1 ;;
  *)   echo "✗ Unexpected response." >&2; exit 1 ;;
esac
