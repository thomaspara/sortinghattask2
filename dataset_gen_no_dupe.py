#post labeling
#randomly picks non dupes
import glob
import pandas as pd
import os
import itertools
import re
from Levenshtein import distance
import random as rand
import math

look_at_folder = ".\SH_data\label_sets\labeled\\*"

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
    file_list = glob.glob(look_at_folder + "\*.csv")
    ds = pd.read_csv("./dataset.csv")

    num_files = len(file_list)
    curr_file = 0
    file_list = file_list[curr_file:]
    
    add_rows = []

    while len(add_rows) < 4400:
        f = file_list[rand.randrange(0,len(file_list))]
        file_list.remove(f)

        df = pd.read_csv(f)
        df_size = len(df)

        col_name = df.columns[0]

        indexes = list(range(0,df_size))
        rand.shuffle(indexes)

        for i in range(0,math.ceil(df_size/2)):
            if len(indexes) < 2: break

            in_1 = indexes.pop()
            in_2 = indexes.pop()
            
            word_1 = df.iloc[in_1]
            word_2 = df.iloc[in_2]

            while( (word_1['group'] == word_2['group']) and word_1['group'] != -1):
                if len(indexes) < 1: 
                    in_2 = -1
                    break
                in_2 = indexes.pop()
                word_2 = df.iloc[in_2]
            
            if in_2 == -1: break

            w_1 = str(word_1[col_name])
            w_2 = str(word_2[col_name])

            add_rows.append(
                pd.Series([
                    False,
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
            

