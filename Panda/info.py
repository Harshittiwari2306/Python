import pandas as pd

# df = pd.read_json("Panda/sample_Data.json")

data = {
    "name":['rohit','kohli','kane','dhoni'],
    "age":[38,37,36,41],
    "city":['mumbai','delhi','newzeland','ranchi']
}

df = pd.DataFrame(data)

print("Displaying the info of data set")

print(df.info())