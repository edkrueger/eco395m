import pandas as pd

df = pd.read_csv("facebook/reaction_counts.csv")

print(df)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())

# print(df.head(3))
# print(df.tail(3))

# print(df.loc[0])
# print(df.loc[0, "status_link"])

# print(df["num_reactions"])
# print(df.loc[:, "num_reactions"])

# print(df.loc[:, ["num_reactions", "num_comments"]])
# print(df[["num_reactions", "num_comments"]])

clean_df = df.set_index("status_id")

print(clean_df)
print(clean_df.loc["153080620724_10157914483265725"])
print(clean_df.dtypes)

# clean_df["status_published"] = pd.to_datetime(clean_df["status_published"])
# print(clean_df.dtypes)

clean_df = clean_df.assign(status_published=lambda df_: pd.to_datetime(df_["status_published"]))
print(clean_df.dtypes)
