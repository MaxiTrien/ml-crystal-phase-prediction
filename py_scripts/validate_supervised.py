# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:07:12 2020

@author: Maxi
"""
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

# load the calculated clusters from a textfile
arr = np.loadtxt('./pred_labels/pred_labels_zro2_0_4_del_better.txt.', dtype=float)

# load files with pickle tool
df_labels_hfo2 = pd.read_pickle('./data_labels/labels_zro2.pkl')

# change the numbers acording the the predicted phases, because of
# random assignment of numbers in clusters
df_labels_hfo2['labels_0_4'] = df_labels_hfo2['labels_0_4'].replace({'m': 1,
                                                                     'p-o': 3,
                                                                     'o': 0,
                                                                     't': 4,
                                                                     'unknown': 2})


df_labels_hfo2['pred_labels'] = np.asarray(arr)
conf_mat = confusion_matrix(df_labels_hfo2['labels_0_4'],
                            df_labels_hfo2['pred_labels'])

acc = np.sum(conf_mat.diagonal()) / np.sum(conf_mat)
print('Overall accuracy: {}%'.format(acc * 100))

f1 = f1_score(df_labels_hfo2['labels_0_4'], 
              df_labels_hfo2['pred_labels'], average='macro')

prec = precision_score(df_labels_hfo2['labels_0_4'], 
                       df_labels_hfo2['pred_labels'], average='macro')
rec = recall_score(df_labels_hfo2['labels_0_4'], 
                   df_labels_hfo2['pred_labels'], average='macro')

print('f1 score : ' +  str(f1))
print('precision score: ' + str(prec))
print('recall score: ' + str(rec))
