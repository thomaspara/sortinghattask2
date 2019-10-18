""" Thomas Parashos 2019
1. Take from the big list of things
2. remove unusabe and numeric (return to unusable later, potential links e.g. employee to id number)
3. make spreadsheet with that data
record_id, y_act, reason, col_name, unique_entry, times_entered, percent_of_total, list_of_rows

This now out to be a collection of methods
"""
import glob
import pandas as pd
from datetime import datetime

###Globals###

#Paths
main_folder = "./SH_data"
source_data_folder = "/datasets"
index_folder = "/meta_data"
prelim_labeled_data_folder = "/data_for_labeling"

data_folder = main_folder + source_data_folder + "/"

index_path = main_folder + index_folder +"/*.csv"
pre_labeled_path = main_folder + prelim_labeled_data_folder + "/reduced_labels.csv"

output_folder = main_folder + "/label_sets/"

log_file = "./log.txt"

#Open Files
log_file = open(log_file, "a+")

#Lists
encodings = [None, "cp1252", "ISO-8859-1"]

###Methods###

def log(log_string):
    log_file.write("[{}]\t".format(datetime.now()) +log_string + "\n")

def p_log(log_string):
    print(log_string)
    log(log_string)

def print_list(l):
    for e in l: print(e)

def multi_read(read_fun, file_list, give_list = False):
    #Returns a df of all the files in the list appended together
    dfs = []
    for path in file_list: 
        try:
            dfs.append(read_fun(path))
        except:
            print("failed to append")
            print(path)
    if give_list: return dfs
    return pd.concat(dfs, sort=False)

def get_subset_eq(df, col_name, val):
    return df.loc[df[col_name] == val]

def read_tsv(file_path, encoding = None):
    return pd.read_csv(file_path, sep = "\t", encoding = encoding)

def glob1(file_path):
    #gives a string of the first file in a glob
    g = glob.glob(file_path)
    len_g = len(g)
    if len_g == 1: return g[0]
    if len_g == 2: 
        print("Multiple files\n", g)
        return g[0]
    if len_g == 0:
        print("no files")
        return g

def col_replace(df, col_name, old_val, new_val):
    #inplace operation
    #replaces all specified values in a df's column with the given input
    df[col_name][df[col_name] == old_val] = new_val

def list_starting_from(tar_list, start_el, skip = 0):
    start = tar_list.index(start_el) + skip
    return tar_list[start:]

def read_csv_mult_encodings(file_path):
    #attempts to read file with each specified encoding in order
    #yells at you if it can't
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding = encoding)
        except: pass
    p_log("Opening Failed. File: "+file_path)
    return None

def write_list(file, string_list):
    for st in string_list:
        file.write(st)

def all_equal(my_list):
    return all(x == my_list[0] for x in my_list)

class Counter:

    def __init__(self, total, name):
        self.i = 0
        self.total = total
        self.name = name

    def inc(self, e_name, prefix):
        self.i += 1
        print("{}{}: {}, {} of {}, {:.2%}".format(prefix, self.name, e_name, self.i, self.total, self.i/self.total))

if __name__ == "__main__":
    # file_list = glob.glob("SH_data\label_sets\labeled\contains_d\*.csv")
    # print(len(file_list))

    # big_df = multi_read(read_csv_mult_encodings, file_list)
    # big_df.to_csv("cdfify.csv")

    # file_list = glob.glob("SH_data\label_sets\labeled\contains_d\*.csv")
    # print(len(file_list))

    # dfs = multi_read(read_csv_mult_encodings, file_list, give_list=True)
    # i_s = []
    # for i in range(0,len(dfs)):
    #     df = dfs[i]
    #     if len(df[df['reason'] == 'ahi']) > 0:
    #         df.to_csv(f"todays_data/{i}.csv")
    #     else:
    #         i_s.append(i)
    # dfs = [dfs[i] for i in i_s ]
    # pd.concat(dfs).to_csv('todays_data/good.csv')
    


    # reason_df = pd.read_csv("todays_data\\10.csv")
    # print(reason_df)
    # reason_df = reason_df[reason_df['reason'] == 'ahi']
    # reason_df.to_csv("todays_data\\10.csv", index=False)


    # import re
    # def alnum(my_str):
    #     return re.sub(r'\W+', '', my_str)

    # df = pd.read_csv("todays_data\\10.csv")
    # start = 1
    # for group in range(start, df["group"].max() + 1):
    #     curr_df = df[df["group"] == group]
    #     print(curr_df)
    #     words = curr_df[curr_df.columns[0]].tolist()

    #     if all_equal([w.lower() for w in words]): new_reason = "a"
    #     elif all_equal([w.replace(" ", "") for w in words]): new_reason = "h"
    #     elif all_equal([alnum(w) for w in words]): new_reason = "i"
    #     elif all_equal([w.lower().replace(" ", "") for w in words]): new_reason = "a h"
    #     elif all_equal([alnum(w).lower() for w in words]): new_reason = "a i"
    #     elif all_equal([alnum(w).replace(" ", "") for w in words]): new_reason = "h i"
    #     elif all_equal([alnum(w).replace(" ", "").lower() for w in words]): new_reason = "a h i"

    #     df.at[df["group"] == group, 'reason'] = new_reason
    #     df.to_csv("todays_data\\10.csv", index=False)

    # file_list = glob.glob("todays_data\\*.csv")
    # dfs = multi_read(read_csv_mult_encodings, file_list)
    # dfs = dfs[dfs['reason'] != "zzz"]
    # dfs = dfs['reason']
    # dfs.to_csv("todays_data\\data.csv")
    # import matplotlib.pyplot as plt
    # df = pd.read_csv("todays_data\\data.csv")
    # plot = df["reason"].value_counts().plot.pie()
    # plt.show()
    # print(df["reason"].value_counts())
    # df["reason"].value_counts().to_csv("todays_data\\counts.csv")

    import matplotlib.pyplot as plt
    df = pd.read_csv("todays_data\\counts.csv", index_col="reason")
    print(df)
    plot = df.plot.pie(y="Reason")
    plt.show()
    # print(df["reason"].value_counts())
    # df["reason"].value_counts().to_csv("todays_data\\counts.csv")








