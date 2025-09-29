import os
import csv
from pprint import pprint

header = ["a", "b", "c"]
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rows = [dict(zip(header, row)) for row in data]

pprint(rows)


outdir = "artifacts"

os.makedirs(outdir, exist_ok=True)

outpath = os.path.join(outdir, "csv_dict.csv")

with open(outpath, "w+") as f:

    dict_writer = csv.DictWriter(f, fieldnames=rows[1].keys())
    dict_writer.writeheader()
    dict_writer.writerows(rows)