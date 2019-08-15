#undoes the current labeling
import pandas as pd
import glob

look_at_folder = ".\SH_data\current_targets"

file_sub = ""

file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")


for f in file_list:
    changed = False
    df = pd.read_csv(f)
    df['group'] = -1
    df['reason'] = 'zzz'
    df.to_csv(f, index = False)
