'''Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.'''

dict = {
        "country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]
       }

import pandas
brics = pandas.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]    # Optionaly. Replace standart index (0, 1, 2, ...) with index that you set in list
print(brics)

# Import the .csv file
cars = pandas.read_csv('cars.csv'[, index_col = 0]) # At which point index should be started

# Show only needed columns
brics[['cars_per_cap', 'county']]

# Show only needed rows
brics[2:4]

# loc is label-based, which means that you have to specify rows and columns based on their row and column labels
brics.loc[['AUS', 'EG']]

# iloc is integer index based, so you have to specify rows and columns by their integer index 
brics.iloc[2]