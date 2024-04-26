import os
import numpy as np
import pandas as pd

print(os.getcwd())
os.chdir('/examples')
print(os.getcwd())
df = pd.read_excel('/examples/example_table.xlsx')


# Print the first few rows of the DataFrame
print(df.head())