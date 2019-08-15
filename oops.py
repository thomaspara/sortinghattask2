#more mistakes
import pandas as pd
import glob
import os

#record = "years"

files = glob.glob(".\SH_data\label_sets\labeled\\contains_d\*.csv")#.format(record))
# nums = []
# for f in files:
#         x = f.split()[0]
#         x = x.split("\\")[-1]
#         nums.append(int(x))
# #         os.rename(f, f.replace("SH_data\label_sets", "to_veiw_later/year"))
# nums = list(set(nums))
# nums.sort()
# print(nums)
# quit()
# indexes = [0]

for f in files:
    df = pd.read_csv(f)
    df_index = df['reason'].tolist()
    try:
        df_index = df["reason"].tolist()
    except:
        os.rename(f, f.replace("label_sets\labeled\\contains_d", "d_no_reason"))
        print("bad moved" +(f))
        continue
    if "f" in df_index:
        os.rename(f, f.replace("label_sets\labeled\\contains_d", "pot_null"))
        print("moved" +(f))
