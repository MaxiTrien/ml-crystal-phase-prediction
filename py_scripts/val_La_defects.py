import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from matminer.featurizers.structure import XRDPowderPattern
import plotly.express as px


def tsne_algo(X, perplexity, labels_true):
    
    from sklearn.manifold import TSNE
    n_components = 3
    Xtsne = TSNE(n_components, perplexity=perplexity).fit_transform(X)
    dftsne = pd.DataFrame(Xtsne)
    dftsne['labels'] = labels_true
    return dftsne


def kmeans_algo(dftsne):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5)
    tsne_labels = kmeans.fit_predict(dftsne[[0, 1, 2]])
    dftsne['cluster'] = tsne_labels
    dftsne.columns = ['x1', 'x2', 'x3', 'labels', 'cluster']
    return dftsne


def sort_clusterlabels(dftsne_kmeans, label_count):
    dftsne_times = dftsne_kmeans.groupby(["labels", "cluster"]).size().reset_index(name="Time")
    
    m_df = dftsne_times[dftsne_times['labels'].str.match('m')]
    po_df = dftsne_times[dftsne_times['labels'].str.match('p-o')]
    o_df = dftsne_times[dftsne_times['labels'].str.match('o')]
    t_df = dftsne_times[dftsne_times['labels'].str.match('t')]
    
    if(label_count == 5):
        unknown_df = dftsne_times[dftsne_times['labels'].str.match('unknown')]
        unk_newlabel = unknown_df.loc[unknown_df['Time'] == unknown_df.Time.max(), 'cluster'].values[0]
        dftsne_kmeans = dftsne_kmeans.replace({'unknown': unk_newlabel})
        
    m_newlabel = m_df.loc[m_df['Time'] == m_df.Time.max(), 'cluster'].values[0]
    po_newlabel = po_df.loc[po_df['Time'] == po_df.Time.max(),'cluster'].values[0] 
    o_newlabel = o_df.loc[o_df['Time'] == o_df.Time.max(), 'cluster'].values[0]
    t_newlabel = t_df.loc[t_df['Time'] == t_df.Time.max(), 'cluster'].values[0]
    
    dftsne_kmeans = dftsne_kmeans.replace({'m': m_newlabel,
                                           'p-o': po_newlabel,
                                           'o': o_newlabel,
                                           't': t_newlabel})
    return dftsne_kmeans


# %%


df = pd.read_pickle(r"C:\Python\Projects\crystal-phase-prediction"
                    r"\pkl_files\structure_labels_La_defects.pkl")

dotants = pd.read_pickle(r'C:\Python\Projects\crystal-phase-prediction'
                         r'\pkl_files\probe_data.pkl')
dot = dotants['dopant']

dot = np.unique(dot)
dot = dot.tolist()
dot.remove('Hf')
dot.remove('La')

labels_true = df['labels_0_3']
df = df.drop(columns=['labels_0_3'])

xrd = XRDPowderPattern(two_theta_range=(5, 65))
df = xrd.fit_featurize_dataframe(df, 'structure')

X = df.iloc[:, 2:]
 
# %%

perplexity = list(range(20, 100, 1))  # perplexity values to test
labels_count = 4  # select number of lables

performance = []
for perplex in perplexity:
    dftsne = tsne_algo(X, perplex, labels_true)
    dftsne_kmeans = kmeans_algo(dftsne)
    dftsne_kmeans = sort_clusterlabels(dftsne_kmeans, labels_count)
    acc = accuracy_score(dftsne_kmeans['labels'], dftsne_kmeans['cluster'])
    performance.append(acc)
    
perf_dic = dict(zip(perplexity, performance))
print('Best value of performance: '
      + str(max(perf_dic.values()))
      + ' Perplexity = '
      + str(max(perf_dic, key=perf_dic.get)))

print(perf_dic)

# %%

fig = px.scatter_3d(dftsne, x='x1', y='x2', z='x3', color=dftsne['labels'], 
                    title='TSNE 3D Ground Truth')
fig.show()
