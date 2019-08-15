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
    start_next = None

    ## open files ##
    index = glob1(index_path)
    pre_labeled = glob1(pre_labeled_path)

    index = pd.read_csv(index)
    pre_labeled = pd.read_csv(pre_labeled)

    ## get list of records ##
    records = pre_labeled["Record_id"].unique()
    records.sort()
    if start_next is not None : records = list_starting_from(records.tolist(), start_next, skip = 1)
    print(records)

    ## go into each record and get the attributes ##
    record_count = Counter(len(records), "Record")
    for record in records:
        ## isolate record in the pre_labeled_csv ##
        df = pre_labeled.loc[pre_labeled['Record_id'] == record] 

        ## get name of record ##
        record_name = index.loc[index['Record_id'] == record]['name'].unique()
        try:
            record_name = record_name[0]
        except:
            print(record_name)
            p_log("failed to obtain record: {}".format(record))
            continue
        record_name = glob1(data_folder+record_name)

        ## get list of attributes ##
        attributes = df['Attribute_name'].unique()

        ## open the record ##
        record_df = read_csv_mult_encodings(record_name, encodings)

        if record_df is None: continue

        ## go into each column for each of the attributes and gather the unique entries ##
        att_count = Counter(len(attributes), "Attribute")
        for attribute in attributes:
            ## get number of appearances for each of the unique entries ##
            entries = record_df[attribute].value_counts()

            ## use data for labeling to get other stats ##
            att_df = df.loc[df['Attribute_name'] == attribute]
            if(att_df.count()[0] > 1):
                print(att_df)
                p_log("Record: {} has the attribute: {}, multiple times".format(record_name, attribute))
                continue

            curr_total = att_df['Total_val'].iloc[0]
            curr_distinct = len(entries)

            ## create the dataframe for the file ##
            att_df = entries.to_frame(name = "times_entered")
            att_df["total"] = curr_total
            att_df["percent_of_entries"] = att_df["times_entered"] / curr_total
            att_df["group"] = -1

            ## make the file ##
            file_name = "{} {} {}".format(curr_distinct, record, attribute)
            if "/" in file_name:
                log("removed / in:" + file_name)
                file_name = file_name.replace("/", "_")
            att_df.to_csv(output_folder + file_name + ".csv", index_label = attribute)

            att_count.inc(attribute, "R: {}, ".format(record))
          
        print("==============================")
        record_count.inc(record, "")
        print("==============================")
