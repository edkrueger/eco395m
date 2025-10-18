import os
import csv

PATH = os.path.join("data", "facebook", "reaction_counts.csv")

with open(PATH, "r") as f:
    
    csv_reader = csv.DictReader(f)

    counts = {}

    for row in csv_reader:

        print(row)

        if row["status_type"] in counts:
            counts[row["status_type"]] += int(row["num_reactions"])
        else:
            counts[row["status_type"]] = int(row["num_reactions"])

    print(counts)




