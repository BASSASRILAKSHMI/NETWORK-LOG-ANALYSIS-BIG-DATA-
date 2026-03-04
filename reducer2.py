#!/usr/bin/env python3
import sys

current_geo = None
total = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 2:
        continue

    geo = parts[0]

    try:
        value = float(parts[1])
    except:
        continue

    if current_geo == geo:
        total += value
        count += 1
    else:
        if current_geo is not None and count > 0:
            avg = total / count
            print(current_geo + "\t" + str(avg))

        current_geo = geo
        total = value
        count = 1

if current_geo is not None and count > 0:
    avg = total / count
    print(current_geo + "\t" + str(avg))