import os

import pandas as pd
from matplotlib import pyplot as plt

IN_PATH = os.path.join("facebook", "reaction_counts.csv")

df = (
	pd.read_csv(IN_PATH)
	.set_index("status_id")
	.assign(status_type=lambda df_: df_["status_type"].astype("category"))
	.assign(status_published=lambda df_: pd.to_datetime(df_["status_published"]))
)

print(df.describe())
print(df.info())

print(
	df.groupby('status_type')["num_reactions"]
	.mean()
	.sort_values(ascending=False)
	.plot(
		kind="bar",
		xlabel="Status Type",
		ylabel="Reactions",
		title="Avg Num Reaction by Status Type")
	)

plt.savefig("num_reactions_by_status_type.png")

print(
	df.groupby('status_type')[df.select_dtypes("number").columns]
	.mean()
	.sort_values("num_reactions", ascending=False)
	.plot(
		kind="bar",
		xlabel="Status Type",
		ylabel="Count",
		title="Count by Status Type")
	)

plt.savefig("counts_by_status_type.png")

# print(df["num_reactions"].sum())
# print(df.select_dtypes("number").sum())



# print(df.sum())

# print(df["status_published"])
# print(df.dtypes)
# square = lambda x: x ** 2
# print(square(4))
# print(df.columns)
# print(df.index)
# print(df["status_type"].unique())
# print(new_df.dtypes)


