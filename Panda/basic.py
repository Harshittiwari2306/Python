import pandas as pd


# df = pd.read_csv("Panda/sales_data_sample (1).csv", encoding="latin1")

df = pd.read_json("Panda/sample_Data.json")

print (df)