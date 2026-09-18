import os
import csv

in_path = os.path.join("facebook", "reaction_counts.csv")
out_path = os.path.join("facebook", "agg_reaction_counts.csv")

with open(in_path) as file:

	reader = csv.DictReader(file)

	total_num_reactions = 0
	total_num_comments = 0
	total_num_shares = 0

	for row in reader:
		total_num_reactions += int(row["num_reactions"])
		total_num_comments += int(row["num_comments"])
		total_num_shares += int(row["num_shares"])

with open(out_path, "w+") as file:
	writer = csv.DictWriter(file, ["total_num_reactions", "total_num_comments", "total_num_shares"])
	writer.writeheader()
	writer.writerow({
			"total_num_reactions": total_num_reactions,
			"total_num_comments": total_num_comments,
			"total_num_shares": total_num_shares

		})