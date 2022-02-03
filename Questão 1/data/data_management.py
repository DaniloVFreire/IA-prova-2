import pandas as pd

df = pd.read_excel('raw_data.xlsx', index_col=1)

df.to_csv('data.csv')