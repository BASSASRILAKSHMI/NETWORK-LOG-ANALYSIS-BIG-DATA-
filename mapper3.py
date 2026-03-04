#!/usr/bin/env python3
import sys

THRESHOLD = 100000.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = [f.strip() for f in line.split(",")]

    if len(fields) < 3:
        continue

    if "Destination Port" in fields[0]:
        continue

    try:
        geo = fields[-1]
        flow_packets = float(fields[15])   # Flow Packets/s column index

        if flow_packets > THRESHOLD:
            print(geo + "\t1")

    except:
        continue


