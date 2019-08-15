#Make the cdfs
import glob
import pandas as pd
import os
import itertools
import re
from Levenshtein import distance
import matplotlib.pyplot as plt

look_at_folder = ".\SH_data\label_sets\labeled\\contains_d"
file_list = glob.glob(look_at_folder + "\*")

lens = []
post_lens = []

for f in file_list:
    df = pd.read_csv(f)
    new_len = len(df)
    lens.append(new_len)
    num_groups = df['group'].max()
    df = df.loc[df['group'] == -1]
    new_len = len(df) + num_groups
    post_lens.append(new_len)

df = pd.read_csv('h.csv')
look_at_folder = ".\SH_data\label_sets\labeled\\no_d"
fl = glob.glob(look_at_folder + "\*")


ones = [1 for i in range(0,len(fl))]
lens = [x + 1 for x in lens]
for i in ones: lens.append(i)
print(lens)

df['pre'] = lens
df['pre'].hist(cumulative=True, density=1, histtype = 'step', linewidth=7.0, label="non-deduplicated", ).set_xscale('log')

#df['post'].hist(cumulative=True, density=1, histtype = 'step', linewidth=7.0, label="deduplicated") 

# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#            ncol=2, mode="expand", borderaxespad=0.)
plt.show()
df.to_csv("h.csv")
print(lens)
print(post_lens)


