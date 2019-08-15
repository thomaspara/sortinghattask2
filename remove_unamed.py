#removes unammed cols in the dataset was a broblem when the index variable in to_csv wasn't set false
import pandas as pd

df = pd.read_csv('./SH_data/data_for_labeling/label_set.csv')

unnames = []

for i in df.columns :
    if "Unnamed" in i: unnames.append(i)

df = df.drop(unnames, axis = 1)

df.to_csv('./SH_data/data_for_labeling/label_set.csv', index=False)

print(df.columns, len(df.columns))