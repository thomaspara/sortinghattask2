#used to fix a whoopsie
import pandas as pd

df = pd.read_csv('./1500 252 County.csv')
thingy = df['County'].value_counts()
print(thingy)