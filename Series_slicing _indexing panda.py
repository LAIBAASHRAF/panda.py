import pandas as pd

list_s = pd.Series([1, 2, 3, 4, 5, 6, 7], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(list_s)             # -----> print Series
print(list_s['c'])       # print value at index 'c'
print(list_s['g'])      # print value at index 'g'
print(list_s['a':'g'])  # Slicing from index 'e' to 'g'   ----> how value at index 'g' is printed
print(list_s['g':'a':-1])    # why it displayed empty list "-1" means backward. which will defiantly return empty as
# starting is before ending.  "Start" is after "Stop" of the series. So It can go backwards

