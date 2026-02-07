#!/bin/sh
set -eu

date
streamripper http://oeins.de:8000/oeins -d /workspace/streamripper/output/music/ -s -r 8001 -l "${1}" -D '%d %S %A %T'