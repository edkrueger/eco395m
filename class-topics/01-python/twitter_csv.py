import os
import csv

PATH = os.path.join("data", "facebook", "reaction_counts.csv")

with open(PATH, "r") as f:
    
    csv_reader = csv.reader(f)

    _ = next(csv_reader)

    counts = {}

    for row in csv_reader:

        status_type = row[3]
        num_reactions = int(row[6])

        if status_type in counts:
            counts[status_type] += num_reactions
        else:
            counts[status_type] = num_reactions

    print(counts)




