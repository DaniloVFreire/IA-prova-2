from chefboost import Chefboost as chef
import pandas as pd

df = pd.read_csv("../data/raw_data.csv")
print(df.head())

config = {'algorithm':'C4.5'}

model = chef.fit(df,config, target_label='Risco')