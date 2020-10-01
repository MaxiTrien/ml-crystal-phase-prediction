# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:55:35 2020

@author: Maxi

Build a dataframe with the crystal structures from the cif files for easy handling with the matminer lib.
"""

import pandas as pd
import numpy as np
import os

def load_data(folder, arr):
    '''
    Load cif files from folder into pymatgen crystal objects and parse them 
    to structures.
    Args:
        folder (string): Where we load the data from.
        arr (list): List of cif filenames in folder.
        x (nparray): representation of 1/angström for powder simulation.

    Returns:
        df (dataframe): representation of structures in pymatgen structure object.
    '''
    from pymatgen.io.cif import CifParser

    file_arr = []
    for file in arr:
        filename = os.sep.join([folder, file])
        parser = CifParser(filename)
        structure = parser.get_structures()[0]
        data = [structure]
        file_arr.append(data)
        
    df = pd.DataFrame(file_arr, columns=['structure'])
    return df

# specify abs path of folder, where you want to load the data from
folder = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\CIFs"
arr = os.listdir('CIFs') # change folder name here

df = load_data(folder, arr)
df['name'] = arr # create column with the filenames in folder


pd.to_pickle(df, './Discriptor_hfo2_del.pkl')

