#!/usr/bin/env python3
import sys

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
        packet_rate = float(fields[-2])   # Packet_Rate column

        if geo:
            print(geo + "\t" + str(packet_rate))
    except:
        continue