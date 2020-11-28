import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.manifold import TSNE

def kmeans_algo(df, n_clusters):
    '''Return the dataframe with predicted kmeans labels.'''
    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(df)
    df['cluster'] = labels
    return df


def pca_algo(X, comp):
    '''Return the PCA from Descriptor X.'''
    pca = PCA(n_components=comp)
    dfpca = pca.fit_transform(X)
    dfpca = pd.DataFrame(dfpca)
    return dfpca


def nmf_algo(X, comp):
    '''Return the Matrix Factorisation from Descriptor X.'''
    model = NMF(n_components=comp, init='random', random_state=0, max_iter = 8000)
    nmf_features_W = model.fit_transform(X)
    nmf_componentes_H = model.components_
    # nmf_df = pd.DataFrame(nmf_componentes_H.T)
    W_df = pd.DataFrame(nmf_features_W) # weights represent abundence of phase at a given nominal composition
    return W_df


def tsne_algo(X, perplex):
    '''Return the TSNE from Descriptor X.''' 
    Xtsne = TSNE(n_components=3, perplexity=perplex).fit_transform(X)
    dftsne = pd.DataFrame(Xtsne)
    return dftsne



