import pandas as pd

df = (
    pd.read_csv("facebook/reaction_counts.csv")
    .assign(status_published=lambda df_: pd.to_datetime(df_["status_published"]))
    .assign(num_negatives=lambda df_: df_["num_sads"] + df_["num_angrys"])
    .set_index("status_id")
)

print(df.info())
print(df["num_reactions"].describe())

print(df["num_reactions"] > 50000)
print(df[df["num_reactions"] > 50000])

print(df["status_published"].dtype)

print(df["status_type"].unique())
print(df["status_type"].value_counts())

print(df.groupby("status_type")["num_reactions"].mean())
print(
    df.groupby("status_type")[
        [
            "num_reactions",
            "num_comments",
            "num_shares",
            "num_likes",
            "num_loves",
            "num_wows",
            "num_hahas",
            "num_sads",
            "num_angrys",
            "num_negatives",
        ]
    ].mean()
)

print(df.set_index("status_published").resample("M")[
            "num_reactions",
            "num_comments",
            "num_shares",
            "num_likes",
            "num_loves",
            "num_wows",
            "num_hahas",
            "num_sads",
            "num_angrys",
            "num_negatives",
        ].sum())
