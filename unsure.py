#move things to an unsure folder
import glob
import os

files = glob.glob("SH_data\current_targets\*.csv")

for f in files : 
    print(f)
    os.rename(f, f.replace("current_targets", "aaa_unsure"))