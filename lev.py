#outputs the nearness of entries in the columns, it will print the entries below the nearness threashold
import pandas as pd
import glob
import sys
from Levenshtein import distance

if len(sys.argv) > 1:
    lev_num = int(sys.argv[1])
else: 
    lev_num = 3

start_num = 0

def j_s(st):
    return ' '.join(st.split())

look_at_folder = ".\SH_data\current_targets"

file_sub = ""

file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")

edited = 0
group_num = 0

for f in file_list:
    changed = False
    df = pd.read_csv(f)
    uni = df[df.columns[0]].tolist()
    uni = [j_s(u) for u in uni]
    uni = list(set(uni))
    labels = []
    group_num = start_num
    for u in uni:
        group_num += 1
        labels.append([u, group_num, "h"])
    
    seen = [[-1,-1]]
    for label in labels:
        targets = ([ distance(j_s(x), label[0]) in range(1,lev_num) for x in df[df.columns[0]] ])
        rows = df.index[targets].tolist()
        if len(rows) < 2 : continue
        if rows in seen: continue
        seen.append(rows)
        rows = df.iloc[rows]
        print("==============")
        print(label[0])
        print(rows)
        for e in rows[rows.columns[0]].tolist():
            print('["{}", ,"b"],'.format(e))