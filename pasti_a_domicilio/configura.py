import os
import numpy as np
import pandas as pd

this_menu = pd.read_excel('examples/menù.xlsx', na_values='NaN')

# Print the first 5 rows of the DataFrame
print(this_menu.head())
print(this_menu.shape[1])

for i, row in this_menu.iterrows():
    #if sum([np.isnan(el) for el in row]) == this_menu.shape[1]:
    if i == 3:
        print([np.isnan(el) for el in row])
    #if sum([np.isnan(el) for el in row]) == this_menu.shape[1]:
    #    this_menu.drop(i)


print(this_menu.shape)