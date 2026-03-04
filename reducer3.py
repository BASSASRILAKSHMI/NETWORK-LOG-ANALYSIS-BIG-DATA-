#!/usr/bin/env python3
import sys

current_geo = None
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 2:
        continue

    geo = parts[0]

    if current_geo == geo:
        count += 1
    else:
        if current_geo is not None:
            print(current_geo + "\t" + str(count))
        current_geo = geo
        count = 1

if current_geo is not None:
    print(current_geo + "\t" + str(count))