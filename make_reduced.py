#takes in the big pre_labeled dataset and makes a dataset where y_act == usable directly categorical
import pandas as pd

pre_labeled = pd.read_csv('./SH_data/data_for_labeling/data_for_labeling.csv')

pre_labeled['y_act'] = pre_labeled['y_act'].str.lower()

pre_labeled.y_act[pre_labeled.y_act == 'usable directly categorical '] = 'usable directly categorical'

pre_labeled = pre_labeled[pre_labeled['y_act'] == 'usable directly categorical']

pre_labeled.to_csv("./SH_data/data_for_labeling/reduced_labels.csv")