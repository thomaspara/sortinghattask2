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
percent_change= []
dup_per_col = []
dupe_group_size = []

for f in file_list:
    df = pd.read_csv(f)
    tot_len = len(df) #num of unique vals, domain size
    lens.append(tot_len)

    groups = df['group'].unique()
    num_groups = len(groups) - 1 #num of groups
    dup_per_col.append(num_groups)

    for g in groups:
        if g == -1 : continue
        group_size = len(df.loc[df['group'] == g])
        dupe_group_size.append(group_size)

    df = df.loc[df['group'] == -1]
    new_len = len(df) + num_groups #non dupes plus num of dupe groups
    post_lens.append(new_len)

    percent_change.append(abs((new_len - tot_len)/tot_len * 100))

fig, ax = plt.subplots(figsize=(8, 4))

n, bins, patches = ax.hist(lens, len(set(lens)), density=True, histtype='step',
                           cumulative=True, label='Non-Deduplicated',  linewidth=3)

ax.hist(post_lens,  len(set(lens)), density=True, histtype='step', cumulative=True,
        label='Deduplicated', linewidth=3)

ax.grid(True)
ax.legend(loc=8)
ax.set_title('Domain Size Shift')
ax.set_xlabel('Domain Size (Number of Unique Values)')
ax.set_ylabel('CDF (Columns)')

plt.show()

###############

fig, ax = plt.subplots(figsize=(8, 4))

n, bins, patches = ax.hist(percent_change, len(set(percent_change)), density=True, histtype='step',
                           cumulative=True,  linewidth=3)


ax.grid(True)
ax.legend(loc=8)
ax.set_title('Percent Change in Domain Size due to Deduplication')
ax.set_xlabel('Percent Change')
ax.set_ylabel('CDF (Columns)')

plt.show()

###############

fig, ax = plt.subplots(figsize=(8, 4))

n, bins, patches = ax.hist(dup_per_col, len(set(dup_per_col)), density=True, histtype='step',
                           cumulative=True,  linewidth=3)


ax.grid(True)
ax.legend(loc=8)
ax.set_title('Duplicate Groups per Column with Duplicates')
ax.set_xlabel('Number of Duplicate Groups')
ax.set_ylabel('CDF (Columns)')

plt.show()

###############

fig, ax = plt.subplots(figsize=(8, 4))

full_list = dup_per_col + [0 for i in glob.glob(".\SH_data\label_sets\labeled\\no_d/*")]

n, bins, patches = ax.hist(full_list, len(set(full_list)), density=True, histtype='step',
                           cumulative=True,  linewidth=3)


ax.grid(True)
ax.legend(loc=8)
ax.set_title('Duplicate Groups per Column')
ax.set_xlabel('Number of Duplicate Groups')
ax.set_ylabel('CDF (Columns)')

plt.show()

###############

fig, ax = plt.subplots(figsize=(8, 4))

n, bins, patches = ax.hist(dupe_group_size, len(set(dupe_group_size)), density=True, histtype='step',
                           cumulative=True,  linewidth=3)


ax.grid(True)
ax.legend(loc=8)
ax.set_title('Size of the Duplicate Groups')
ax.set_xlabel('Number of Elements in the Duplicate Group')
ax.set_ylabel('CDF (Groups)')

plt.show()














quit()

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


