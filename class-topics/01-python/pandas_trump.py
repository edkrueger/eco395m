import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data/facebook/reaction_counts.csv").assign(
    status_published=lambda df_: pd.to_datetime(df_["status_published"])
)

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
        ]
    ].median()
)

print(
    df.set_index("status_published")
    .resample("1M")[
        "num_reactions",
        "num_comments",
        "num_shares",
        "num_likes",
        "num_loves",
        "num_wows",
        "num_hahas",
        "num_sads",
        "num_angrys",
    ]
    .sum()
    .plot()
)

plt.savefig("artifacts/trump_growth.png")


# print(df.columns)
# print(df.tail())
# print(df.dtypes)

# print(df["status_published"])
# print(pd.to_datetime(df["status_published"]))
# print(df.columns)
# print(df.dtypes)

# print(df["status_published"])

# print(df["status_type"].unique())
# print(df["status_type"].value_counts())

# print(df["num_comments"].mean())
# print(df["num_comments"].median())
# print(df["num_comments"].describe())

# print(
#     df[
#         [
#             "num_reactions",
#             "num_comments",
#             "num_shares",
#             "num_likes",
#             "num_loves",
#             "num_wows",
#             "num_hahas",
#             "num_sads",
#             "num_angrys",
#         ]
#     ].describe()
# )
