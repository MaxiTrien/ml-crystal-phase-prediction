# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:56:21 2020

@author: Maxi

"""

import numpy as np
import pandas as pd

# where is the file located 
df = pd.read_csv(r'C:\Python\Projects\crystal-phase-prediction\crystal_data\overview.csv')

# Data cleaning
clean_df = df[['dopant', 'host, type', 'nominal concentration [f.u.%]',
               'abc [sc]', 'phase', 'crit. overall']].copy()

# replacing the phasenumbers with names
clean_df['phase'].replace({14: 'm', 29: 'p-o', 61: 'o', 137: 't'},
                          inplace=True)

print(clean_df['crit. overall'].value_counts())

# all columns exept for crit. overall into on string collum as id
clean_df['ID'] = clean_df['dopant'].str.cat(clean_df['host, type'], sep='_')

# make a new collum out of important string features
clean_df['ID1'] = clean_df['dopant'].astype(str) \
                + '_' + clean_df['host, type'].astype(str) \
                + '_' + clean_df['nominal concentration [f.u.%]'].astype(str) \
                + '_' + clean_df['abc [sc]'].astype(str) \
                + '_' + clean_df['phase']

clean_df = clean_df[['ID1', 'crit. overall']].copy()
clean_df['ID1'] = clean_df['ID1'].str.replace(', ', '_')
clean_df = clean_df.rename(columns={'ID1': 'ID', 'crit. overall': 'labels'})
clean_df = clean_df.sort_values('ID')

clean_df_hfo2 = clean_df[clean_df['ID'].str.contains('HfO2')]
clean_df_zro2 = clean_df[clean_df['ID'].str.contains('ZrO2')]

# reset the index of the dataframe
clean_df_hfo2.reset_index(drop=True, inplace=True)
clean_df_zro2.reset_index(drop=True, inplace=True)

# get everything after the last underscore
clean_df_hfo2['labels_0_3'] = clean_df_hfo2['ID'].str.extract(r'([^_]+$)')
clean_df_zro2['labels_0_3'] = clean_df_zro2['ID'].str.extract(r'([^_]+$)')


clean_df_hfo2['labels_0_4'] = clean_df_hfo2['labels_0_3'].copy()
clean_df_hfo2.loc[clean_df_hfo2['labels'] == False, 'labels_0_4'] = 'unknown'
clean_df_zro2['labels_0_4'] = clean_df_zro2['labels_0_3'].copy()
clean_df_zro2.loc[clean_df_zro2['labels'] == False, 'labels_0_4'] = 'unknown'

clean_df_hfo2 = clean_df_hfo2.drop(columns=['labels'])
clean_df_zro2 = clean_df_zro2.drop(columns=['labels'])

# set the abs path 
clean_df_hfo2.to_pickle('C:\Python\Projects\crystal-phase-prediction\data_labels\labels_hfo2.pkl')
clean_df_zro2.to_pickle('C:\Python\Projects\crystal-phase-prediction\data_labels\labels_zro2.pkl')

