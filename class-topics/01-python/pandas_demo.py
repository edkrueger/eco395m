import pandas as pd

series1 = pd.Series(
    index=[1, 2],
    data=[3, 4],
    name="series1"
)

series2 = pd.Series(
    index=[1, 2],
    data=[5, 6],
    name="series2"
)

series3 = pd.Series(
    index=[1, 3],
    data=[5, 6],
    name="series2"
)

# print(series1)
# print(list(series1.index))
# print(list(series1.values))
# print(series1.sum())
# print(series1.mean())
# print(series1.median())
# print(series1.std())

# print(series1 + series2)
# print((series1 * series2).sum())

# print(series1 + series3)

df = pd.DataFrame([series1, series2]).T
print(df)

df2 = pd.DataFrame({
    "id": [1,2],
    "value1": [3, 4],
    "value2": [5, 6]
}).set_index("id")

# print(df2)

df3 = pd.DataFrame({
    "value1": [3, 4],
    "value2": [5, 6]
},
index=[1,2])

# print(df3)

print(df["series2"])
print(type(df["series2"]))
print(df["series2"][2])
print(df.loc[2, "series2"])
print(df.iloc[1, 1])

print(df.loc[2])