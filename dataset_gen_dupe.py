#post labeling
#uses every column with dupes, goes through every group, then goes through every combonation of pairings in each group, and adds those to the dataset
import glob
import pandas as pd
import os
import itertools
import re
from Levenshtein import distance

look_at_folder = ".\SH_data\label_sets\labeled\\contains_d"

def has_letters(st):
    return bool( re.match( '[a-zA-Z]', st ) )

def case_a(st_1, st_2):
    return st_1.lower() == st_2.lower()

def case_h(st_1, st_2):
    t_1 = ' '.join(st_1.split())
    t_2 = ' '.join(st_2.split())
    return t_1 == t_2 

regex = re.compile('[^a-zA-Z0-9\*]')

def case_i(st_1, st_2):
    t_1 = regex.sub('', st_1.lower().replace("&", "and"))
    t_2 = regex.sub('', st_2.lower().replace("&", "and"))
    return t_1 == t_2 

if __name__ == "__main__":
    file_list = glob.glob(look_at_folder + "\*")
    print(len(file_list))
    quit()
    ds = pd.read_csv("./dataset.csv")

    num_files = len(file_list)
    curr_file = 0
    file_list = file_list[curr_file:]
    for f in file_list:
        df = pd.read_csv(f)
        df = df.loc[df['group'] != -1]
        col_name = df.columns[0]
        add_rows = []

        for group in df['group'].unique():
            group_df = df.loc[df['group'] == group]

            for comb in itertools.combinations(list(range(0,len(group_df))), 2):
                word_1 = group_df.iloc[comb[0]]
                word_2 = group_df.iloc[comb[1]]
                w_1 = str(word_1[col_name])
                w_2 = str(word_2[col_name])

                add_rows.append(
                    pd.Series([
                        True,
                        w_1,
                        w_2,
                        col_name,
                        word_1['percent_of_entries'],
                        word_2['percent_of_entries'],
                        len(w_1),
                        len(w_2),
                        distance(w_1,w_2),
                        has_letters(w_1),
                        has_letters(w_2),
                        case_a(w_1, w_2),
                        case_h(w_1, w_2),
                        case_i(w_1, w_2)
                    ], index = ds.columns)
                )

        ds = ds.append(add_rows , ignore_index=True)
        curr_file += 1
        print(f)
        print(curr_file, "/", num_files, num_files-curr_file, 'left')
        ds.to_csv("./dataset.csv", index = False)
            

