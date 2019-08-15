#merged with task two
#increments the current number for the dataset list
import pandas as pd

df = pd.read_csv("./current_num.csv")
num = df['curr'][0] + 1
df['curr'] = num 
print(num, "of", 263)
print(263 - num, "left")
df.to_csv("./current_num.csv", index=False)
