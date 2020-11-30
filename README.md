# ml-crystal-phase-prediction

> Prediction of crystal phase from DFT data with cluster analysis and supervised learning methods.


![Alt text](docs/2Dcluster_TSNE_xrd_low.png "Title")

## Instructions: 

1. Select data from data/crystal_data/ folder
2. For changing the crystal objects (atoms or angles) --> change_angles.py, change_oxygen.py
    - Otherwise you can skip that step..
3. From cif format build structure object
    - File in other formats: convert to cif file with "infile_tocif.py"
    - Then build structure object
3. Select Descriptor XRD/PRDF (Build PRDF.ipynb, Build XRD.ipynb)
4. Run specific algorithm (example: Kmeans_DR_XRD.ipynb)

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


><a id="1">[1]</a> L. P. René de Cotret, M. R. Otto, M. J. Stern. and B. J. Siwick, *An open-source software ecosystem for the interactive exploration of ultrafast electron scattering data*, Advanced Structural and Chemical Imaging 4:11 (2018) [DOI: 10.1186/s40679-018-0060-y.](https://ascimaging.springeropen.com/articles/10.1186/s40679-018-0060-y)

><a id="2">[2]</a> Ward, L., Dunn, A., Faghaninia, A., Zimmermann, N. E. R., Bajaj, S., Wang, Q.,
Montoya, J. H., Chen, J., Bystrom, K., Dylla, M., Chard, K., Asta, M., Persson,
K., Snyder, G. J., Foster, I., Jain, A., Matminer: An open source toolkit for
materials data mining. Comput. Mater. Sci. 152, 60-69 (2018).

><a id="3">[3]</a> Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

### Contributors
Maximilian Trien
University of Applied Science Munich
