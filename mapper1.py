#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = [f.strip() for f in line.split(",")]

    # Skip header safely
    if len(fields) < 3:
        continue

    if "Destination Port" in fields[0]:
        continue

    try:
        geo = fields[-1]
        failed = int(float(fields[-3]))

        if geo and failed >= 0:
            print(geo + "\t" + str(failed))

    except:
        continue