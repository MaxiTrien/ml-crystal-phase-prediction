# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:42:06 2020

@author: Maxi

Classification with functional data
"""

from ase.io import read
from crystals import Crystal
from skued import powdersim
import os
from skfda import FDataGrid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.model_selection import (train_test_split, GridSearchCV)
from sklearn.model_selection import StratifiedShuffleSplit
from skfda.ml.classification import KNeighborsClassifier
import skfda.preprocessing.smoothing.kernel_smoothers as ks
import skfda.preprocessing.smoothing.validation as val
from sklearn.model_selection import cross_val_score

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
        
        diff = powdersim(crys, x, fwhm_l=50)
        diff_norm = diff / diff.max()
        crys_arr.append(diff_norm)
        
    crys_arr = np.array(crys_arr)
    fd = FDataGrid(crys_arr, x,
                   dataset_name='Diffraction Curves',
                   argument_names=[r'$q (1/\AA)$'],
                   coordinate_names=['Diffracted intensity (A.u.)'])
    print(fd)
    
    return fd


def smooth_datagrid(fd):
    '''
    Smoothes the values in the datagrid object

    Args:
        fd (datagrid): Includes data_matrix, x vector for contionous data
        representation.

    Returns:
        knn_fd (datagrid): datagrid values smoothed with an kN Kernel.

    '''
    # smooth the values with kNeighbors kernel
    param_values = np.linspace(start=2, stop=25, num=24)
    knn = val.SmoothingParameterSearch(ks.KNeighborsSmoother(), param_values)
    knn.fit(fd)
    knn_fd = knn.transform(fd)
    
    return knn_fd

# %%

folder = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\CIFs"
arr = os.listdir('CIFs')
x = np.linspace(1, 4, 1000)
# change for hfo2 and zro2
df_labels = pd.read_pickle(r'C:\Python\Projects\crystal-phase-prediction\data_labels\labels_all.pkl')
labels = df_labels['new_labels']
fd = load_datagrid_sim(folder, arr, x)
fd_knn = smooth_datagrid(fd)

# %%
X_train, X_test, y_train, y_test = train_test_split(fd_knn, labels, 
                                                    test_size= 0.30,
                                                    stratify= labels,
                                                    random_state=0)


param_grid = {'n_neighbors': np.arange(2, 30, 1)}
knn = KNeighborsClassifier(metric='euclidean', multivariate_metric=True)
ss = StratifiedShuffleSplit(n_splits=5, test_size=.25, random_state=0)
gscv = GridSearchCV(knn, param_grid, cv=ss)
gscv.fit(fd_knn, labels)

print("Best params:", gscv.best_params_)
print("Best score:", gscv.best_score_)
# %%
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(param_grid['n_neighbors'], gscv.cv_results_['mean_test_score'])
ax.set_xticks(param_grid['n_neighbors'])
ax.set_ylabel("Number of Neighbors")
ax.set_xlabel("Test score")
ax.set_ylim((0.85, 0.93))
plt.show()
# %%

knn = KNeighborsClassifier(n_neighbors=10, metric='euclidean', 
                           multivariate_metric=True)

scores = cross_val_score(knn, fd_knn, labels, cv=10)
print(scores)
print('Accuracy: %0.2f (+- %0.2f)' %(scores.mean(), scores.std() * 2))