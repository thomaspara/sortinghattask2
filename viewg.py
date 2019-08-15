#lets you veiw the labeled groups
import pandas as pd
import glob

look_at_folder = ".\SH_data\current_targets"

file_sub = ""

file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")


for f in file_list:
    changed = False
    df = pd.read_csv(f)
    df = df.loc[df['group'] != -1]
    df[df.columns[0]] = df[df.columns[0]].str.lower()
    df = df.sort_values(df.columns[0])
    df = df.sort_values('group')
    print(df)
    quit()