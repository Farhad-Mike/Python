dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

from numpy import array_equiv
import pandas as pd 
brics = pd.DataFrame(dict)
brics.index = [1, 2, 3, 4, 5]

area = brics[['country', 'capital']]

print(brics[1:3])