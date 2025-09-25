import os
import csv

header = ["a", "b", "c"]
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
outdir = "artifacts"

os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "csv.csv")

with open(outpath, "w+") as f:

    csv_writer = csv.writer(f)

    csv_writer.writerow(header)

    for row in data:
        csv_writer.writerow(row)





