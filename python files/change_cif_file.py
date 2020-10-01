# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:20:12 2020

@author: Maxi
"""

from ase.io import read, write
import os


def change_spec_elements(folder, target_folder, arr, element):
    '''
    Load cif files from folder into ase crystal objects, change all elements 
    O with specific other elements
    Args:
        folder (string): Where we load the data from.
        arr (list): List of cif filenames in folder.
        x (nparray): representation of 1/angström for powder simulation.

    Returns:
        fd (datagrid): representation of intensity values and 1/angström
        values in datagrid object.

    '''
    filename_arr = []
    j = 0
    for file in arr:
        filename = os.sep.join([folder, file])
        filename_arr.append(file)
        structure = read(filename)
        symbols = structure.get_chemical_symbols()
        i = 0
        for symbol in symbols:
            if symbol == 'O':
                structure.symbols[i] = element
            i = i + 1
            
        print(structure.get_chemical_symbols())
        print(a)
        target_path = os.sep.join([target_folder, file])
        write(target_path, structure)
        j = j + 1
        
# select the element you want to switch in crystal
element = 'Hf'
folder = r'C:\Python\Projects\crystal-phase-prediction\hfo2' # load data from this folder 
arr = [f for f in os.listdir(folder) if not f.endswith('.ini')] # ignore hidden files in folder
target_folder = r'C:\Python\Projects\crystal-phase-prediction\hfo2_del' # file where to store the new cif files

change_spec_elements(folder, target_folder, arr, element)



