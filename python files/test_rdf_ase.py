# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:44:01 2020

@author: Maxi
"""


from ase.io import read
from ase.geometry.analysis import Analysis
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
    

filename = r"C:\Users\Maxi\Desktop\m\Ag_HfO2_inter_3.125_222_m.cif"
filename1 = r"C:\Users\Maxi\Desktop\CIFs_pure\pure_HfO2_m.cif"

labels = pd.read_pickle('./data_labels/labels_hfo2.pkl')

crystal = read(filename)
crystal1 = read(filename1)

corrdinates = crystal.get_positions()
cell_length = crystal.get_cell_lengths_and_angles()
cell_length = cell_length[0:3]  # only select the cell length

dr = 0.01  # shperical shell radius dr
min_length_cell = min(cell_length)  # select the smalles length in cell
 
rmax = (min_length_cell / 2) - 0.1 #  2*rmax < min_length_cell

bins = np.rint((min_length_cell / 3) * 100)
bins = bins.astype(int)
rdf = Analysis(crystal)
rdf2 = Analysis(crystal1)
g = rdf.get_rdf(rmax, bins)
g_r = rdf.get_rdf(rmax, bins)
r = np.linspace(0, rmax, bins)

y1 = np.array(g)
y = np.array(g_r)

y1 = np.transpose(y1)
y = np.transpose(y)
print(np.count_nonzero(y))
plt.figure()
plt.plot(r, y, color='black')
plt.plot(r, y1, color='blue')
plt.xlabel('r')
plt.ylabel('g(r)')
plt.xlim((0, rmax))
# plt.ylim((0, 1.05 * y.max()))
plt.show()
