from chefboost import Chefboost as chef
import pandas as pd

df = pd.read_csv("regras_c4_5.csv")
df.columns = df.columns.str.upper()

for column in df.columns:
    df[column] = df[column].str.lower()

# print(df.head())

config = {'algorithm': 'C4.5'}
model = chef.fit(df.copy(), config, 'RISCO')

# -------------------------
# Evaluate  train set
# -------------------------
# Accuracy:  95.0 % on  20  instances
# Labels:  ['alto' 'moderado' 'baixo']
# Confusion matrix:  [[8, 0, 0], [0, 6, 0], [1, 0, 5]]
# Decision  alto  => Accuray:  95.0 %, Precision:  100.0 %, Recall:  88.8889 %, F1:  94.1177 %
# Decision  moderado  => Accuray:  100.0 %, Precision:  100.0 %, Recall:  100.0 %, F1:  100.0 %
# Decision  baixo  => Accuray:  95.0 %, Precision:  83.3333 %, Recall:  100.0 %, F1:  90.9091 %