#!/bin/bash

DAY=$1
ANS=$2

curl "https://adventofcode.com/2022/day/${DAY}/answer" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'cookie: _ga=GA1.2.310135606.1669835766; _gid=GA1.2.247416144.1669835766; session=53616c7465645f5f3a17c2fabecca3cde0b37968fcc99be41048ae585b7722974276708f56512803868d2c796c9c07841cc259153a6d352d6e4ae73a18f01838' \
  -H 'origin: https://adventofcode.com' \
  -H "referer: https://adventofcode.com/2022/${DAY}/7" \
  -H 'sec-ch-ua: "Chromium";v="106", "Not.A/Brand";v="24", "Opera GX";v="92"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0' \
  --data-raw "level=1&answer=${ANS}" \
  --compressed