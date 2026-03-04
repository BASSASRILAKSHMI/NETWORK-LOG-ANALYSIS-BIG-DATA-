#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = [f.strip() for f in line.split(",")]

    if len(fields) < 2:
        continue

    # Skip header
    if "Destination Port" in fields[0]:
        continue

    try:
        label = fields[-4]   # Label column position

        if label:
            print(label + "\t1")
    except:
        continue