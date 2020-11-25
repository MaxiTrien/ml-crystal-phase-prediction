from ase.io import read
from ase.visualize import view
import matplotlib.pyplot as plt
import numpy as np
from skued import powdersim
from crystals import Crystal
import numpy as np
import pandas as pd
import os

def load_datagrid_sim(folder, arr, x):
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
    crys_arr = []
    for file in arr:
        filename = os.sep.join([folder, file])
        filename_arr.append(file)
        crys = read(filename)
        crys = Crystal.from_ase(crys)
        
        diff = powdersim(crys, x)
        diff_norm = diff / diff.max()
        crys_arr.append(diff_norm)
        
    crys_arr = np.array(crys_arr)
    
    print(crys_arr)

    return crys_arr

folder = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\hfo2_del"
arr = os.listdir(r"C:\Python\Projects\crystal-phase-prediction\crystal_data\hfo2_del")
x = np.linspace(1, 4, 300)
diff = load_datagrid_sim(folder, arr, x)
np.save(r"C:\Python\Projects\crystal-phase-prediction\pkl_files\diffsim_hfo2_del.pkl", diff)