#!/usr/bin/env python3
import sys

current_geo = None
total = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 2:
        continue

    geo = parts[0]

    try:
        value = int(parts[1])
    except:
        continue

    if current_geo == geo:
        total += value
    else:
        if current_geo is not None:
            print(current_geo + "\t" + str(total))
        current_geo = geo
        total = value

if current_geo is not None:
    print(current_geo + "\t" + str(total))