import pandas as pd

data = {
    "name":['rohit','kohli','kane','dhoni'],
    "age":[38,37,36,41],
    "city":['mumbai','delhi','newzeland','ranchi']
}

df = pd.DataFrame(data)
print(data)

df.to_json("output.json",indent=False)