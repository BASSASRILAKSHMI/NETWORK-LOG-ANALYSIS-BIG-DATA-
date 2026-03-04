#!/usr/bin/env python3
import sys

current_label = None
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 2:
        continue

    label = parts[0]

    if current_label == label:
        count += 1
    else:
        if current_label is not None:
            print(current_label + "\t" + str(count))
        current_label = label
        count = 1

if current_label is not None:
    print(current_label + "\t" + str(count))