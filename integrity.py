#moves things into the oops folder
#i make some mistakes
import glob
import pandas as pd
import os

look_at_folder = ".\oops"

if __name__ == "__main__":
    m_file_list = glob.glob(look_at_folder + "\*")
    m_bad = 0
    yeet = 0

    for m_f in m_file_list:

        m_df = len(pd.read_csv(m_f).columns)
        if m_df == 6:
            os.rename(m_f, m_f.replace("oops", "SH_data\label_sets\labeled\\no_d"))
        # if 'reason' not in m_df.columns:
        #     m_df['reason'] = 'zzz'
        #     #os.rename(m_f, m_f.replace("oops", "SH_data\label_sets\labeled\\no_d"))
        #     m_bad += 1
        #     m_df.to_csv(m_f, index = False)
            yeet += 1

    print("=================")
    print(yeet, m_bad)