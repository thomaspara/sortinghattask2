# if the current targets contain a custon null, move it to a folder to veiw later
import glob
import os

files = glob.glob("SH_data\current_targets\*.csv")

for f in files : 
    print(f)
    os.rename(f, f.replace("current_targets", "pot_null"))