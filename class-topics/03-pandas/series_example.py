import pandas as pd

s = pd.Series(data=[1, 4, 7], index=["d", "e", "f"])
s2 = pd.Series(data=[2, 5, 8], index=["d", "e", "f"])
s3 = pd.Series(data=[2, 5, 8], index=["a", "b", "c"])
s4 = pd.Series(data=[2, 5, 8], index=["d", "b", "c"])

print(s)
print(s.index)
print(s.values)

print(s.loc["e"])

print(s > 3)

print(s[s > 3])

print(s + s2)
print(s + s3)
print(s + s4)

print(s * s2)
print(s * 2)
