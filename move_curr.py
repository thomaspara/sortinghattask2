#merged with task2
#moves curent to either no_d or contains_d based on whether or not it contains groups
import glob
import pandas as pd
import os

look_at_folder = ".\SH_data\current_targets"

if __name__ == "__main__":
    m_file_list = glob.glob(look_at_folder + "\*")
    
    m_group = 0
    m_no_group = 0

    for m_f in m_file_list:
        m_df = pd.read_csv(m_f)
        m_col = m_df["group"].tolist()
        if 1 in m_col:
            m_group += 1
            os.rename(m_f, m_f.replace("current_targets", "label_sets/labeled/contains_d"))
        else:
            m_no_group += 1
            os.rename(m_f, m_f.replace("current_targets", "label_sets/labeled/no_d"))

    print("Contains Dupe:", m_group)
    print("No Dupe:", m_no_group)


