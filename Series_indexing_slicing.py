import pandas as pd

list_s =pd.Series([1,2,3,4,5,6,7],index =['a','b','c','d','e','f','g'],dtype=int,name="Data_column")

# print(list_s)  -----> print Series

print(list_s['c'])       # print value at index 'c'
print(list_s['g'])      # print value at index 'g'
print(list_s['a':'g'])  # Slicing from index 'e' to 'g'   ----> how value at index 'g' is printed it violates the rule of slicing
print(list_s['g':'a':-1])    # why it displayed empty list
