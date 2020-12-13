# ml-crystal-phase-prediction

> Prediction of crystal phase from Hfo2/Zro2 data with cluster analysis and supervised learning methods.

![](docs/recording.gif)

## Instructions: 

1. Select data from data folder
2. For changing the crystal object (atoms or angles) use: [change_angles.py](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/py_scripts/change_angles.py), [change_oxygen.py](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/py_scripts/change_oxygen.py)
3. From cif format build [structure object](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/py_scripts/df_build_descriptorsetup.py):
    - File in other formats: convert to cif file with [infile_tocif.py](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/py_scripts/infile_tocif.py)
    - Afterwards build structure object
3. Select Descriptor XRD/PRDF in different specifications: [Build PRDF.ipynb](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/notebooks/unsupervised%20models/PRDF/Build%20PRDF.ipynb), [Build XRD.ipynb](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/notebooks/unsupervised%20models/XRD-Pattern/Build_XRD.ipynb)
4. Run specific algorithm, for example: [Kmeans_DR_XRD.ipynb](https://github.com/MaxiTrien/ml-crystal-phase-prediction/blob/master/notebooks/unsupervised%20models/XRD-Pattern/Kmeans_DR_XRD.ipynb)

## Content: 
 
 - Data Cleaning
 - Data Exploration
 - Functional Data Analysis
 - Clusteranalysis
 - Data Reduction Methods (PCA, NMF, TSNE)
 - Visualization 2D, 3D
 
 ## Installation
 - Clone this repo to your local machine using `https://github.com/MaxiTrien/crystal-phase-prediction.git`

### Authors and acknowledgment

><a id="1">[1]</a> Falkowski, M., Künneth, C., Materlik, R. et al. Unexpectedly large energy variations from dopant interactions in ferroelectric HfO2 from high-throughput ab initio calculations. npj Comput Mater 4, 73 (2018). https://doi.org/10.1038/s41524-018-0133-4

><a id="2">[2]</a> L. P. René de Cotret, M. R. Otto, M. J. Stern. and B. J. Siwick, *An open-source software ecosystem for the interactive exploration of ultrafast electron scattering data*, Advanced Structural and Chemical Imaging 4:11 (2018) [DOI: 10.1186/s40679-018-0060-y.](https://ascimaging.springeropen.com/articles/10.1186/s40679-018-0060-y)

><a id="3">[3]</a> Ward, L., Dunn, A., Faghaninia, A., Zimmermann, N. E. R., Bajaj, S., Wang, Q.,
Montoya, J. H., Chen, J., Bystrom, K., Dylla, M., Chard, K., Asta, M., Persson,
K., Snyder, G. J., Foster, I., Jain, A., Matminer: An open source toolkit for
materials data mining. Comput. Mater. Sci. 152, 60-69 (2018).


### Contributors
Maximilian Trien \
At Laboratory for modeling and simulation \
University of Applied Science Munich 
