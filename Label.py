#labels based on the list of labels you give it
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
    log_file.write("["+datetime.now()+"]\t"+ log_string + "\n")

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

    labels = [
        # ["", , "b"],

        ["US Ambassador Residence", 2,"b"],
        ["US Ambasador Residence", 2,"b"],
        # ["Limnos", 1, "b"],
        # ["Lemnos", 1, "b"],
        # ["Chalkidiki", 2, "b"],          
        # ["Halkidiki", 2, "b"],
        # ["Assyrtico", 3, "b"],
        # ["Assyrtiko", 3, "b"],
        # ["Xinisteri", 4, "b"],
        # ["Xynisteri", 4, "b"],
        # ["Aragonês", 5, "b"],
        # ["Aragonez", 5, "b"],
        # ["Muscadel", 6, "b"],
        # ["Muscatel", 6, "b"],
        # ["Chardonelle", 7, "b"],
        # ["Chardonel", 7, "b"],
        # ["Moschofilero", 8, "b"],
        # ["Moscofilero", 8, "b"],
        # ["Carignan", 9, "b"],
        # ["Carignano", 9, "b"],
        # ["Carignane", 9, "b"],
        # ["Malagousia", 10,"b"],
        # ["Malagouzia", 10,"b"],
        # ["Sylvaner", 11,"b"],
        # ["Silvaner", 11,"b"],
        # ["Rosato", 12,"b"],
        # ["Rosado", 12,"b"],
        # ["Cerceal", 13,"b"],
        # ["Cercial", 13,"b"],
        # ["Tinta de Toro", 14,"b"],
        # ["Tinta del Toro", 14,"b"],

        # ["1999 ATS euro / euro", 1, "h"],
        # ["1999 ATS euro / euro                    ", 1, "h"],
        # ["1999 BEF euro / euro", 2, "h"],
        # ["1999 BEF euro / euro                    ", 2, "h"],
        # ["1999 DEM euro / euro", 3, "h"],
        # ["1999 DEM euro / euro                    ", 3, "h"],
        # ["1999 ESP euro / euro", 4, "h"],
        # ["1999 ESP euro / euro                    ", 4, "h"],
        # ["1999 FIM euro / euro", 5, "h"],
        # ["1999 FIM euro / euro                    ",5 , "h"],
        # ["1999 FRF euro / euro", 6, "h"],
        # ["1999 FRF euro / euro                    ", 6, "h"],
        # ["1999 IEP euro / euro      ", 7, "h"],
        # ["1999 IEP euro / euro                    ", 7, "h"],
        # ["1999 ITL euro / euro", 8, "h"],
        # ["1999 ITL euro / euro                    ", 8, "h"],
        # ["1999 NLG Euro / Euro     ", 9, "a h"],
        # ["1999 NLG euro / euro                    ", 9, "a h"],
        # ["1999 PTE euro / euro", 10, "h"],
        # ["1999 PTE euro / euro                    ", 10, "h"],
        # ["2001 GRD euro / euro", 11, "h"],
        # ["2001 GRD euro / euro                    ", 11, "h"],
        # ["Argentine peso", 12, "h"],
        # ["Argentine peso                          ", 12, "h"],
        # ["Australian dollar", 13, "h"],
        # ["Australian dollar     ", 13, "h"],
        # ["Australian dollar                       ", 13, "h"],
        # ["Australian Dollars                      ", 13, "h"],
        # ["Bahrain dinar", 14, "h"],
        # ["Bahrain dinar                           ", 14, "h"],
        # ["CFA Franc", 15, "a h"],
        # ["CFA franc", 15, "a h"],
        # ["CFA franc                               ", 15, "a h"],
        # ["Canadian dollar", 16, "h"],
        # ["Canadian dollar                         ", 16, "h"],
        # ["Chilean peso", 17, "h"],
        # ["Chilean peso                            ", 17, "h"],
        # ["Colombian peso", 18, "h"],
        # ["Colombian peso                          ", 18, "h"],
        # ["Costa Rican colon", 19, "h"],
        # ["Costa Rican colon                       ", 19, "h"],
        # ["Czech koruna", 20, "h"],
        # ["Czech koruna                            ", 20, "h"],
        # ["Danish Krone", 21, "a h"],
        # ["Danish krone", 21, "a h"],
        # ["Danish krone                            ", 21, "a h"],
        # ["Estonian Kroon", 22, "a h"],
        # ["Estonian kroon", 22, "a h"],
        # ["Estonian kroon                          ", 22, "a h"],
        # ["Hong Kong dollar", 23, "h"],
        # ["Hong Kong dollar                        ", 23, "h"],
        # ["Icelandic króna", 24, "h"],
        # ["Icelandic króna       ", 24, "h"],
        # ["Icelandic króna                         ", 24, "h"],
        # ["Iranian rial", 25, "h"],
        # ["Iranian rial                            ", 25, "h"],
        # ["Korean won", 26, "h"],
        # ["Korean won                              ", 26, "h"],
        # ["Mexican new peso", 27, "h"],
        # ["Mexican new peso                        ", 27, "h"],
        # ["Namibia dollar", 28, "h"],
        # ["Namibia dollar                          ", 28, "h"],
        # ["New Zealand dollar", 29, "j h"],
        # ["New Zealand dollar                      ", 29, "j h"],
        # ["New Zealand Dollars", 29, "j h"],
        # ["New Zealand Dollars                     ", 29, "j h"],
        # ["Norwegian krone", 30, "h"],
        # ["Norwegian krone    ", 30, "h"],
        # ["Norwegian krone                         ", 30, "h"],
        # ["Philippine peso", 31, "h"],
        # ["Philippine peso                         ", 31, "h"],
        # ["Romanian Leu", 32, "a"],
        # ["Romanian leu", 32, "a"],
        # ["Russian rouble", 33, "b"],
        # ["Russian ruble", 33, "b"],
        # ["Slovak Koruna       ", 34, "a h"],
        # ["Slovak koruna                           ", 34, "a h"],
        # ["Sri Lanka rupee", 35, "h"],
        # ["Sri Lanka rupee                         ", 35, "h"],
        # ["Swedish Krona", 36, "a h"],
        # ["Swedish Krona     ", 36, "a h"],
        # ["Swedish krona                           ", 36, "a h"],
        # ["Tunisian Dinar", 37, "a"],
        # ["Tunisian dinar", 37, "h"],
        # ["US dollar", 38, "h"],
        # ["US dollar                               ", 38, "h"],
        # ["Yemeni rial", 39, "h"],
        # ["Yemeni rial                             ", 39, "h"],
        # ["Yuan Renminbi", 40, "h"],
        # ["Yuan Renminbi    ", 40, "h"],
        # ["kuna", 41, "h"],
        # ["kuna                                    ", 41, "h"],
        # ["litas", 42, "a h"],
        # ["litas                                   ", 42, "a h"],
        # ["Litas", 42, "a h"],
        # ["loti", 43, "h"],
        # ["loti                                    ", 43, "h"],
        # ["metical", 44, "h"],
        # ["metical                                 ", 44, "h"],
        # ["new sheqel", 45, "h"],
        # ["new sheqel                              ", 45, "h"],
        # ["pound sterling", 46, "h"],
        # ["pound sterling                          ", 46, "h"],
        # ["pula                                    ", 47, "h"],
        # ["rand", 48, "a h"],
        # ["rand                                    ", 48, "a h"],
        # ["Rand", 48, "a h"],
        # ["yen", 49, "h"],
        # ["yen                                     ", 49, "h"],
        # ["zloty    ", 50, "a h"],
        # ["zloty                                   ", 50, "a h"],
        # ["Zloty", 50, "a h"],
        # ["Zloty                 ", 50, "a h"],
        # ["Azerbaijan manat", 51, "h"],
        # ["Azerbaijan manat                        ", 51, "h"],
        # ["bolivar", 52, "h"],
        # ["bolivar                                 ", 52, "h"],
        # ["Cyprus pound", 53, "h"],
        # ["Cyprus pound                            ", 53, "h"],
        # ["córdoba", 54, "h"],
        # ["córdoba      ", 54, "h"],
        # ["deutsche mark", 55, "h"],
        # ["deutsche mark                           ", 55, "h"],
        # ["Dominican peso", 56, "h"],
        # ["Dominican peso                          ", 56, "h"],
        # ["Euro", 57, "h"],
        # ["euro", 57, "h"],
        # ["forint                                  ", 58, "h"],
        # ["Forint", 58, "h"],
        # ["Indian rupee", 59, "h"],
        # ["Indian rupee                            ", 59, "h"],
        # ["lempira", 60, "h"],
        # ["lempira                                 ", 60, "h"],
        # ["leone", 61, "h"],
        # ["leone                                   ", 61, "h"],
        # ["Leone", 61, "h"],
        # ["Maltese liri", 62, "h"],
        # ["Maltese liri                            ", 62, "h"],
        # ["Moldovan leu", 63, "h"],
        # ["Moldovan leu                            ", 63, "h"],
        # ["pataca                                  ", 64, "h"],
        # ["Pataca", 64, "h"],
        # ["ringgit", 65, "h"],
        # ["ringgit   ", 65, "h"],
        # ["ringgit                                 ", 65, "h"],
        # ["Swiss franc", 66, "h"],
        # ["Swiss franc                             ", 66, "h"],
        # ["vatu", 67, "h"],
        # ["vatu                                    ", 67, "h"],
        # ["Zambia kwacha                           ", 68, "j h"],
        # ["Zambian Kwacha", 68, "j h"],
        # ["baht", 69, "h"],
        # ["baht                                    ", 69, "h"],
        # ["balboa", 70, "h"],
        # ["balboa                                  ", 70, "h"],
        # ["Bermuda dollar", 71, "h"],
        # ["Bermuda dollar                          ", 71, "h"],
        # ["EC dollar", 72, "h"],
        # ["EC dollar                               ", 72, "h"],
        # ["Lilangeni", 73, "a"],
        # ["lilangeni                               ", 73, "a"],
        # ["Mauritian rupee", 74, "h"],
        # ["Mauritian rupee                         ", 74, "h"],
        # ["Netherlands Antillean guilder", 75, "h"],
        # ["Netherlands Antillean guilder           ", 75, "h"],
        # ["Ouguiya", 76, "j h"],
        # ["Ouguiyas                                ", 76, "j h"],
        # ["Pakistan Rupee", 77, "a h"],
        # ["Pakistan rupee", 77, "a h"],
        # ["Pakistan rupee                          ", 77, "a h"],
        # ["pakistan rupee", 77, "a h"],
        # ["Seychelles rupee", 78, "h"],
        # ["Seychelles rupee                        ", 78, "h"],
        # ["taka", 79, "h"],
        # ["taka                                    ", 79, "h"],
        # ["Tanzania shilling                       ", 80, "j h"],
        # ["Tanzanian Shilling", 80, "j h"],
        # ["tolar", 81, "h"],
        # ["tolar                                   ", 81, "h"],

        # ["AK", 1, "e"],
        # ["AL", 2, "e"],
        # ["ALABAMA", 2, "e"],
        # ["ALASKA", 1, "e"],
        # ["AR", 3, "e"],
        # ["ARIZONA", 4, "e"],
        # ["ARKANSAS", 3, "e"],
        # ["AZ", 4, "e"],
        # # ["BC", 57, "e"],
        # # ["BRITISH COLUMBIA", 57, "e"],
        # ["CA", 5, "e"],
        # ["CALIFORNIA", 5, "e"],
        # ["CO", 6, "e"],
        # ["COLORADO", 6, "e"],
        # ["CONNECTICUT", 7, "e"],
        # ["CT", 7, "e"],
        # ["DC", 8, "e"],
        # ["DE", 9, "e"],
        # ["DELAWARE", 9, "e"],
        # ["DISTRICT OF COLUMBIA", 8, "e"],
        # # ["FEDERATED STATES OF MICRONESIA", , "e"],
        # ["FL", 10, "e"],
        # ["FLORIDA", 10, "e"],
        # ["GA", 11, "e"],
        # ["GEORGIA", 11, "e"],
        # ["GU", 12, "e"],
        # ["GUAM", 13, "e"],
        # ["HAWAII", 14, "e"],
        # ["HI", 14, "e"],
        # ["IA", 15, "e"],
        # ["ID", 16, "e"],
        # ["IDAHO", 16, "e"],
        # ["IL", 17, "e"],
        # ["ILLINOIS", 17, "e"],
        # ["IN", 18, "e"],
        # ["INDIANA", 18, "e"],
        # ["IOWA", 15, "e"],
        # ["KANSAS", 19, "e"],
        # ["KENTUCKY", 20, "e"],
        # ["KS", 19, "e"],
        # ["KY", 20, "e"],
        # ["LA", 21, "e"],
        # ["LOUISIANA", 21, "e"],
        # ["MA", 22, "e"],
        # ["MAINE", 23, "e"],
        # ["MARSHALL ISLANDS", 57, "e"],
        # ["MARYLAND", 24, "e"],
        # ["MASSACHUSETTS", 22, "e"],
        # ["MD", 24, "e"],
        # ["ME", 23, "e"],
        # ["MH", 57, "e"],
        # ["MI", 25, "e"],
        # ["MICHIGAN", 25, "e"],
        # ["MINNESOTA", 26, "e"],
        # ["MISSISSIPPI", 27, "e"],
        # ["MISSOURI", 28, "e"],
        # ["MN", 26, "e"],
        # ["MO", 28, "e"],
        # ["MONTANA", 29, "e"],
        # ["MP", 54, "e"],
        # ["MS", 27, "e"],
        # ["MT", 29, "e"],
        # ["NC", 30, "e"],
        # ["ND", 31, "e"],
        # ["NE", 32, "e"],
        # ["NEBRASKA", 32, "e"],
        # ["NEVADA", 33, "e"],
        # ["NEW HAMPSHIRE", 34, "e"],
        # ["NEW JERSEY", 35, "e"],
        # ["NEW MEXICO", 36, "e"],
        # ["NEW YORK", 37, "e"],
        # ["NH", 34, "e"],
        # ["NJ", 35, "e"],
        # ["NM", 36, "e"],
        # ["NORTH CAROLINA", 30, "e"],
        # ["NORTH DAKOTA", 31, "e"],
        # ["NORTHERN MARIANA ISLANDS", 54, "e"],
        # ["NV", 33, "e"],
        # ["NY", 37, "e"],
        # ["OH", 38, "e"],
        # ["OHIO", 38, "e"],
        # ["OK", 39, "e"],
        # ["OKLAHOMA", 39, "e"],
        # ["OR", 40, "e"],
        # ["OREGON", 40, "e"],
        # ["PA", 41, "e"],
        # ["PENNSYLVANIA", 41, "e"],
        # ["PR", 42, "e"],
        # ["PUERTO RICO", 42, "e"],
        # ["RHODE ISLAND", 43, "e"],
        # ["RI", 43, "e"],
        # ["SC", 44, "e"],
        # ["SD", 45, "e"],
        # ["SOUTH CAROLINA", 44, "e"],
        # ["SOUTH DAKOTA", 45, "e"],
        # ["TENNESSEE", 46, "e"],
        # ["TEXAS", 47, "e"],
        # ["TN", 46, "e"],
        # ["TX", 47, "e"],
        # ["UT", 48, "e"],
        # ["UTAH", 48, "e"],
        # ["VA", 49, "e"],
        # ["VERMONT", 50, "e"],
        # ["VI", 55, "e"],
        # ["VIRGIN ISLANDS", 55, "e"],
        # ["VIRGINIA", 49, "e"],
        # ["VT", 50, "e"],
        # ["WA", 51, "e"],
        # ["WASHINGTON", 51, "e"],
        # ["WEST VIRGINIA", 52, "e"],
        # ["WI", 53, "e"],
        # ["WISCONSIN", 53, "e"],
        # ["WV", 52, "e"],
        # ["WY", 56, "e"],
        # ["WYOMING", 56, "e"],
    ]

    file_sub = ""

    file_list = glob.glob(look_at_folder + "\\" + file_sub + "*")

    edited = 0

    for f in file_list:
        changed = False
        df = pd.read_csv(f)
        for label in labels:
            rows = df.index[df[df.columns[0]].astype(str) == label[0]].tolist()
            for row in rows:
                if (df.iloc[row]['group'] != -1) : 
                    continue
                df.iat[row, 4] = label[1]
                df.iat[row, 5] = label[2]
                if not changed : changed = (len(rows) > 0)


        if (changed):
            df.to_csv(f, index = False)
            edited += 1
            print(f)

    print("Edited", edited, "files")
