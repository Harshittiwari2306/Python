import pandas as pd

data = {
    "name":['rohit','kohli','jaiswal','dhoni','head','kane','stokes'],
    "age":[38,36,24,41,32,36,36],
    "avg":[40,50,30,35,36,38,45],
    "strike rate":[130,95,98,102,115,80,95]
}

df =  pd.DataFrame(data)

print("sample dataframe")
print(df)

print("Names(single column return series)")
name = df["name"]
print(name)

# subset = df[["name","avg",'age','strike rate']]
# print('\nSubset with Name and salary')
# print(subset)
