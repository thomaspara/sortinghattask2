#used to label and move the labeled column files
import glob
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os


###Globals###

#Paths
main_folder = "./SH_data"
source_data_folder = "/datasets"
index_folder = "/meta_data"
prelim_labeled_data_folder = "/data_for_labeling"

data_folder = main_folder + source_data_folder + "/"

index_path = main_folder + index_folder +"/*.csv"
pre_labeled_path = main_folder + prelim_labeled_data_folder + "/reduced_labels.csv"
entries_path = main_folder + prelim_labeled_data_folder + "/label_set.csv"

output_folder = main_folder + "/label_sets/"

log_file = "./log.txt"

#Open Files
log_file = open(log_file, "a+")

#Lists
encodings = [None, "cp1252", "ISO-8859-1"]

###Methods###

def log(log_string):
    log_file.write("["+datetime.now()+"]\t"+log_string + "\n")

def p_log(log_string):
    print(log_string)
    log(log_string)

def print_list(l):
    for e in l: print(e)

def multi_read(read_fun, file_list):
    #Returns a df of all the files in the list appended together
    dfs = []
    for path in file_list: 
        try:
            dfs.append(read_fun(path))
        except:
            print("failed to append")
            print(path)
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

def read_csv_mult_encodings(file_path, encoding_list):
    #attempts to read file with each specified encoding in order
    #yells at you if it can't
    for encoding in encoding_list:
        try:
            return pd.read_csv(file_path, encoding = encoding)
        except: pass
    p_log("Opening Failed. File: "+file_path)
    return None

def write_list(file, string_list):
    for st in string_list:
        file.write(st)

class Counter:

    def __init__(self, total, name):
        self.i = 0
        self.total = total
        self.name = name

    def inc(self, e_name, prefix):
        self.i += 1
        print("{}{}: {}, {} of {}, {:.2%}".format(prefix, self.name, e_name, self.i, self.total, self.i/self.total))

if __name__ == "__main__":
    # #add col to csv
    # file_list = glob.glob(output_folder + "*.csv")
    # file_list = list_starting_from(file_list, "./SH_data/label_sets\99 178 Police District.csv", 1)
    # for f in file_list:
    #     print(f)
    #     df = pd.read_csv(f)
    #     df['reason'] = 'zzz'
    #     df.to_csv(f, index=False)
    #     print(f)

    ## move things outta curr ##
    print("================================")

    
    look_at_folder = ".\SH_data\current_targets"

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
    print("================================")

    ## load in next set ##

    num_uni = pd.read_csv("./current_num.csv")
    num_uni = num_uni['curr'][0]
    num_uni = [24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 75, 77,
79, 81, 82, 84, 86, 87, 88, 91, 93, 94, 95, 96, 97, 99, 102, 103, 104, 105, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118, 124, 130, 131, 139, 144, 148, 151, 152, 155, 158, 159, 163, 164, 167, 169, 170, 171, 180, 181, 182, 190, 191, 193, 194, 195, 201, 202, 203, 205, 208, 209, 211, 212, 213, 215, 218, 220, 223, 224, 225, 227, 231, 233, 238, 239, 243, 254, 259, 264, 268, 269, 278, 283, 286, 291, 293, 305, 317, 322, 339, 341, 343, 351, 354, 364, 369, 375, 378, 384, 388, 397, 411, 425, 440, 455, 522, 602, 626, 632, 634,
649, 700, 707, 731, 738, 789, 880, 893, 905, 928, 955, 961, 1055, 1111, 1169, 1217, 1229, 1236, 1293, 1362, 1382, 1401, 1431, 1484, 1500, 1623, 1635, 1704, 1788, 1804, 1838, 1930, 2163, 2235, 2282, 2292, 2323, 2328, 2360, 2398, 2417, 2508, 2542, 2670, 2712, 2827, 2918, 2923, 3082, 3288, 3428, 3993, 4276, 4372, 4732, 4851, 4896, 5573, 5642, 5997, 6544,
6557, 6985, 7292, 8286, 8307, 8384, 8874, 9429, 9504, 9526, 9620, 10620, 11007, 11614, 12695, 12699, 13220, 13553, 16125, 16510, 16973, 17936, 18759, 21403, 21851, 24631, 25165, 26384, 29155, 32215, 37979, 39414, 42239, 43159, 43348, 46049, 48680, 49220, 52957, 59495, 71333, 75308, 77911, 180030, 181495, 219509, 454028, 601268, 790696][num_uni]

    file_list = glob.glob(output_folder + "{} *".format(num_uni))
    moved = 0
    uni_entries = []
    move = True

    try:
        f1 = file_list[0]
    except:
        print("\nNo files, possibly time to increment\n")
        print("files labeled with dupes:", len(glob.glob(output_folder + "/labeled/contains_d/*.csv")))
        print("files labeled with no dupes:", len(glob.glob(output_folder + "/labeled/no_d/*.csv")))
        print("files left:", len(glob.glob(output_folder + "*.csv")))
        print("================================")
        df = pd.read_csv("./current_num.csv")
        num = df['curr'][0] + 1
        df['curr'] = num 
        print(num, "of", 263)
        print(263 - num, "left")
        df.to_csv("./current_num.csv", index=False)
        quit()

    df1 = pd.read_csv(f1)
    col1 = df1.columns[0]
    target_entries = df1[col1].tolist()
    target_entries.sort()
    target_entries = [str(x) for x in target_entries]
    target_entries = [x.lower() for x in target_entries]

    index = pd.read_csv(glob1(index_path))

    for f in file_list:
        df = pd.read_csv(f)
        col = df.columns[0]
        entries = df[col].tolist()
        entries.sort()
        entries = [str(x) for x in entries]
        entries = [x.lower() for x in entries]

        if entries == target_entries:
            record_id = int(f.split()[1])
            file_name = index[index['Record_id'] == record_id]["name"].iloc[0]
            link = index[index['Record_id'] == record_id]["link"].iloc[0]
            print(f, "\t", "./SH_data/datasets/"+file_name, "\t", link)
            if move:
                moved += 1
                os.rename(f, f.replace("label_sets", "current_targets"))
        else:
            if entries not in uni_entries:
                uni_entries.append(entries)
    
    target_entries.sort()
    print("================================")
    print_list(target_entries[:100])
    print("================================")
    print("Moved", moved, "files |", len(file_list), "left")
