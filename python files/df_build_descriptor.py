# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:55:35 2020

@author: Maxi
"""

import pandas as pd
import numpy as np
import os
from matminer.featurizers.structure import RadialDistributionFunction

def load_data(folder, arr):
    '''
    Load cif files from folder into ase crystal objects, simulate crystal
    diffraction and represent data in timeseries
    Args:
        folder (string): Where we load the data from.
        arr (list): List of cif filenames in folder.
        x (nparray): representation of 1/angström for powder simulation.

    Returns:
        fd (datagrid): representation of intensity values and 1/angström
        values in datagrid object.

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


folder = r"C:\Python\Projects\Thesis\Test" # change folder name here
arr = os.listdir('Test') # change folder name here

df = load_data(folder, arr)
df['name'] = arr

pd.to_pickle(df, './Discriptor_hfo2_del.pkl')

# radial distribution function feature
# rdf = RadialDistributionFunction(cutoff=10, bin_size=0.05)
# df = rdf.featurize_dataframe(df, 'structure')

