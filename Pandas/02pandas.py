import pandas as pd
import csv
data = pd.read_csv("../placement.csv")
# print(data)
# print(data.describe())
# print(data.info())
data_clean = data.dropna()
print(data_clean)
# print(data["specialisation"])