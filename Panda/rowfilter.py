import pandas as pd


data = {
    "name":['rohit','kohli','jaiswal','dhoni','head','kane','stokes'],
    "age":[38,36,24,41,32,36,36],
    "avg":[41,50,30,35,36,38,45],
    "strike rate":[130,95,98,102,115,80,95]
}

df = pd.DataFrame(data)

high_salary = df[df['avg'] > 40]

print("player with avg greater than 40")
print(high_salary)


filtered = df[(df['avg'] > 44) & (df['age'] > 35)]

print(filtered)

filtere = df[(df['avg'] > 44) | (df['age'] > 30)]

print(filtere)