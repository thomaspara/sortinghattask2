#go through the col and mark any weird capitalization as dupes
import pandas as pd
import glob
import sys

if len(sys.argv) > 1:
    start_num = int(sys.argv[1])
else: 
    start_num = 0


look_at_folder = ".\SH_data\current_targets"

file_sub = ""

file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")

edited = 0
group_num = 0

for f in file_list:
    changed = False
    df = pd.read_csv(f)
    uni = df[df.columns[0]].astype(str).str.lower().tolist()
    uni = [l for l in uni if uni.count(l) > 1]
    uni = list(set(uni))
    labels = []
    group_num = start_num
    for u in uni:
        group_num += 1
        labels.append([u, group_num, "a"])
    for label in labels:
        rows = df.index[df[df.columns[0]].astype(str).str.lower() == label[0]].tolist()
        for row in rows:
            if (df.iloc[row]['group'] != -1) : 
                continue
            df.iat[row, 4] = label[1]
            df.iat[row, 5] = label[2]
            if not changed : changed = (len(rows) > 0)


    if (changed):
        df.to_csv(f, index = False)
        edited += 1
        print(f)

print("Edited", edited, "files")
print("Created", group_num, "groups")
