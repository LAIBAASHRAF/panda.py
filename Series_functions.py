import pandas as pd

list_1 = pd.Series([1, 2, 3, 4, 5])
# print(list_1)
list_2 = pd.Series([19, 12, 3, 43, 89])
# print(list_2)
print(max(list_2))
print(min(list_1))
print(list_1 < 7)      # objection required
print([list_2 < 7])   # objection required
x = list_1 + list_2
print(x)
list_3 = pd.Series([1, 2, 6, 8, 7, 9, 3])
y = list_1 + list_3
print(y)
