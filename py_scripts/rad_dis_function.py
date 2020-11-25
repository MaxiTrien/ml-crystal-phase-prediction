# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:28:04 2020

@author: Maxi
"""
import numpy as np
from ase.io import read
from RDF_3D import pairCorrelationFunction_3D
import matplotlib.pyplot as plt
    

filename = r"C:\Users\Maxi\Desktop\t\Ag_HfO2_cat_3.125_222_t.cif"
crystal = read(filename)
corrdinates = crystal.get_positions()
cell_length = crystal.get_cell_lengths_and_angles()
cell_length = cell_length[0:3]  # only select the cell length

dr = 0.01  # shperical shell radius dr
min_length_cell = min(cell_length)  # select the smalles length in cell
rmax = min_length_cell / 10
x = corrdinates[:, 0]  # split the 2d array into x, y, z coordinates
y = corrdinates[:, 1]
z = corrdinates[:, 2]

g_r, r, ref_ind = pairCorrelationFunction_3D(x, y, z, min_length_cell, rmax, dr)

plt.figure()
plt.plot(r, g_r, color='black')
plt.xlabel('r')
plt.ylabel('g(r)')
plt.xlim( (0, rmax) )
plt.ylim( (0, 1.05 * g_r.max()) )
plt.show()
