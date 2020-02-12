# Pandas Basics

'''
Pandas DataFrames
Pandas is a high-level data manipulation tool developed by Wes McKinney.
It is built on the Numpy package and its key data structure is called the DataFrame.
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

There are several ways to create a DataFrame. One way way is to use a dictionary. For example:
'''

dict_a = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict_a)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

#
'''
Another way to create a DataFrame is by importing a csv file using Pandas. Now, the csv cars.csv is stored and can be imported using pd.read_csv:

Unnamed: 0  cars_per_cap        country drives_right
     area    capital       country  population
0   8.516   Brasilia        Brazil      200.40
1  17.100     Moscow        Russia      143.50
2   3.286  New Dehli         India     1252.00
3   9.597    Beijing         China     1357.00
4   1.221   Pretoria  South Africa       52.98
'''
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv') # file not presented

# Print out cars
print(cars)

'''
<script.py> output:
      Unnamed: 0  cars_per_cap        country drives_right
    0         US           809  United States         True
    1        AUS           731      Australia        False
    2        JAP           588          Japan        False
    3         IN            18          India        False
    4         RU           200         Russia         True
    5        MOR            70        Morocco         True
    6         EG            45          Egypt         True
'''