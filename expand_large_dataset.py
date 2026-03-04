import pandas as pd
import numpy as np
import random

input_file = "cic_original.csv"
output_file = "big_logs_5GB.csv"

chunk_size = 200000
replications = 4

print("Starting enhanced dataset expansion...")

with open(output_file, "w", newline='', encoding="utf-8") as outfile:
    first_write = True

    for r in range(replications):
        print(f"Replication {r+1} started...")

        for chunk in pd.read_csv(input_file, chunksize=chunk_size, low_memory=False):

            # Add Synthetic Source IP
            chunk["Source_IP"] = [
                f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
                for _ in range(len(chunk))
            ]

            # Add Synthetic Destination IP
            chunk["Destination_IP"] = [
                f"10.0.{random.randint(1,255)}.{random.randint(1,255)}"
                for _ in range(len(chunk))
            ]

            # Add Failed Login Attempts
            chunk["Failed_Login_Attempts"] = np.random.poisson(3, len(chunk))

            # Add Packet Rate (simulate traffic spikes)
            chunk["Packet_Rate"] = np.random.normal(500, 150, len(chunk))

            # Add Geo Location
            chunk["Geo_Location"] = np.random.choice(
                ["India", "US", "Germany", "China", "Russia"],
                len(chunk)
            )

            chunk.to_csv(
                outfile,
                mode="a",
                header=first_write,
                index=False
            )

            first_write = False

print("Enhanced 5GB dataset created successfully.")