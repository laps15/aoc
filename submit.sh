#!/bin/bash

YEAR=$1
DAY=$2
LEVEL=$3
ANS=$4

FROM_CWD=$(dirname $0)
SESSION=$(cat ${FROM_CWD}/.session)

curl "https://adventofcode.com/${YEAR}/day/${DAY}/answer" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H "${SESSION}" \
  -H 'origin: https://adventofcode.com' \
  -H 'pragma: no-cache' \
  -H "referer: https://adventofcode.com/${YEAR}/day/${DAY}" \
  -H 'sec-ch-ua: "Chromium";v="118", "Opera GX";v="104", "Not=A?Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition std-1)' \
  --data-raw "level=${LEVEL}&answer=${ANS}" \
  --compressed
