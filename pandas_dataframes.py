import pandas as pd

# Creating DataFrame:"pandas DataFrame is 2D, size mutable,potentially heterogeneous,tabular dataStructure with
# labeled axes (rows and columns)

lis = pd.DataFrame()  # empty DataFrame
print(lis)

lis_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # create DataFrame using list
print(pd.DataFrame(lis_1))

# If I want to print more than one column then I use list of list or 2D Array  to   create  DataFrame

lis_2 = [['Laiba', 20, 'Female', 1], ['Any', 23, 'Female', 3], ['Akaash', 25, 'Male', 5]]
print(pd.DataFrame(lis_2))

# Creating DataFrame using Dictionary_of_list

lis_2 = {'ID': [1, 2, 3], 'Name': ['Laiba', 'Any', 'Akaash'], 'Age': [20, 23, 25],
         'Gender': ['Female', 'Female', 'Male'],
         'Friends': [1, 3, 5]}          # Arrays must be of the  same length
print(pd.DataFrame(lis_2))

#  creating DataFrame using list of dictionary

lis_3 = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
print(pd.DataFrame(lis_3))

#  if unequal values in dictionary then answer of that label will be Nan (pandas fun to handle missing data)

lis_4 = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5}]  # why 'c' print float of 3
print(pd.DataFrame(lis_4))

# Create DataFrame using Dictionaries of Series

lis_4 = {'ID': pd.Series([1, 2, 3, 4]), 'Name': pd.Series(['Laiba', 'Any', 'Akaash', 'Mahi'])}
print(pd.DataFrame(lis_4))

# Creating DataFrame using list of Tuples:

lis_5 = [(1, 2, 3, 4), (5, 6, 7, 8)]
print(pd.DataFrame(lis_5))
