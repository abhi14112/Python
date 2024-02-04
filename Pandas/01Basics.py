import pandas as pd
import numpy as np

wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")
# print(wh["Precipitation amount (mm)"].mean())
# result = wh.drop("Time zone",axis=1).head()
wh["Rainy"] = wh["Precipitation amount (mm)"] > 5
print(wh)
# print(wh.head())
# print(result)