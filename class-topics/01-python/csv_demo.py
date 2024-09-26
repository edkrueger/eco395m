import os
import csv

IN_PATH = os.path.join("data", "facebook", "reaction_counts.csv")
OUT_PATH = os.path.join("data", "facebook", "agg_reaction_counts.csv")

agg_data = {
    "num_reactions": 0,
    "num_comments": 0
}

with open(IN_PATH, "r") as in_file1:

    dict_reader = csv.DictReader(in_file1)

    for row in dict_reader:
        agg_data["num_reactions"] += int(row["num_reactions"])
        agg_data["num_comments"] += int(row["num_comments"])

with open(OUT_PATH, "w+") as outfile:
    dict_writer = csv.DictWriter(outfile, fieldnames=["num_reactions", "num_comments"])
    dict_writer.writeheader()
    dict_writer.writerow(agg_data)
