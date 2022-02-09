from chefboost import Chefboost as chef
import pandas as pd

df = pd.read_csv("regras_cart.csv")
df.columns = df.columns.str.upper()

for column in df.columns:
    df[column] = df[column].str.lower()

# print(df.head())
# print(df)
config = {'algorithm': 'CART'}
model = chef.fit(df.copy(), config, 'RISCO')

# -------------------------
# Evaluate  train set
# -------------------------
# Accuracy:  100.0 % on  20  instances
# Labels:  ['alto' 'moderado' 'baixo']
# Confusion matrix:  [[9, 0, 0], [0, 6, 0], [0, 0, 5]]
# Decision  alto  => Accuray:  100.0 %, Precision:  100.0 %, Recall:  100.0 %, F1:  100.0 %
# Decision  moderado  => Accuray:  100.0 %, Precision:  100.0 %, Recall:  100.0 %, F1:  100.0 %
# Decision  baixo  => Accuray:  100.0 %, Precision:  100.0 %, Recall:  100.0 %, F1:  100.0 %