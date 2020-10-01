# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:20:12 2020

@author: Maxi
"""

from ase.io import read, write
import os


def load_datagrid_sim(folder, target_folder, arr):
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
    filename_arr = []
    a = 0
    for file in arr:
        filename = os.sep.join([folder, file])
        filename_arr.append(file)
        structure = read(filename)
        symbols = structure.get_chemical_symbols()
        i = 0
        for symbol in symbols:
            if symbol == 'O':
                structure.symbols[i] = 'Hf'
            i = i + 1
            
        print(structure.get_chemical_symbols())
        print(a)
        target_path = os.sep.join([target_folder, file])
        write(target_path, structure)
        a = a + 1
        

folder = r'C:\Python\\Projects\Thesis\hfo2' 
arr = [f for f in os.listdir(folder) if not f.endswith('.ini')]
target_folder = r'C:\Python\\Projects\Thesis\Hfo2_new'   
load_datagrid_sim(folder, target_folder, arr)



