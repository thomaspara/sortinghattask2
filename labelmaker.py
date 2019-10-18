#prints a copyable list of labes for label.py
import pandas as pd
import glob

look_at_folder = ".\SH_data\current_targets"

file_sub = ""

file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")

for f in file_list:
    df = pd.read_csv(f)
    entries = df[df.columns[0]].tolist()
    entries.sort()
    for e in entries:
        print('["{}", , "b"],'.format(e))
    quit()