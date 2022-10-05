import pandas as pd

"""create Series in pandas: 'A Pandas Series is like a column in a table. It is a one-dimensional array holding data 
of any type'"""
# parameters of Series method:
#    pd.Series([data/list] ,index=[value],dtype=int/float,name='data_colum_name')
list_s = pd.Series([1, 3, 6, 'k', 45.3])
print(list_s)
# change index of Series up to our choice
list_s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(list_s1)
# change data _type of series
list_s2 = pd.Series([1, 2, 3, 4, 5], index=[0, 1, 2, 3, 4], dtype=float)
print(list_s2)
# Give name of your data colum/Series
list_s3 = pd.Series([109, 22, 36, 10, 5], index=[0, 1, 2, 3, 4], dtype=int, name='Data')
print(list_s3)
# using single  scalar values
scalar_s = pd.Series(34)
print(scalar_s)
# using sequence of scalar values
scalar_s1 = pd.Series(34, index=[2, 3, 4], dtype=float, name='Scalar_data')  # index will copy 34 three times
print(scalar_s1)
# print Series using dictionaries:
scalar_s = pd.Series({'a': 3, 'b': 4, 'c': 34, 'd': 87})
print(scalar_s)
