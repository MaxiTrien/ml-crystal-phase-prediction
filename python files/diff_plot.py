from ase.io import read
from crystals import Crystal
from skued import powdersim
import os
import numpy as np
import matplotlib.pyplot as plt

from skfda import FDataGrid
from skfda.exploratory.visualization.clustering import plot_clusters
from skfda.ml.clustering import KMeans
import skfda.preprocessing.smoothing.kernel_smoothers as ks
import skfda.preprocessing.smoothing.validation as val


aa


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


def kmeans_algo(knn_fd, n_clusters, savefile):
    '''
    Computes n clusters and labels for timeseries data
    
    Args:
        knn_fd (datagrid): smoothed timeseries data.
        n_clusters (int): number of clusters.
        savefile (string): name and location where you want to save the labels.

    Returns:
        None.

    '''
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(knn_fd)
    pred_labels = kmeans.predict(knn_fd)
    np.savetxt(savefile, pred_labels, fmt='%f')
    print(pred_labels)
    plot_clusters(kmeans, knn_fd)
    plt.show()
    

folder = r"C:\Python\Projects\Thesis\zro2_new" # change folder name here
arr = os.listdir('zro2_new') # change folder name here
x = np.linspace(1, 4, 1000)

fd = load_datagrid_sim(folder, arr, x)
knn_fd = smooth_datagrid(fd)

# doc where you want to save the cluster predictions
savefile = r'C:\\Python\\Projects\\Thesis\\pred_labels\\pred_labels_zro2_0_4_del_better.txt'
n_clusters = 5

kmeans_algo(knn_fd, n_clusters, savefile)
