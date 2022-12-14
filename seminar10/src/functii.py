import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy.cluster.hierarchy import linkage, dendrogram # linkage-> fct. pentru clusterizare(???)
from sklearn.cluster._agglomerative import AgglomerativeClustering # -> fct de partitionare(???)

def nan_replace_t(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

def calcul_ierarhie(x, metoda="complete"):
    h = linkage(x, method=metoda) # h -> matricea de ierarhie
    nr_jonctiuni = h.shape[0]
    k_max = np.argmax(h[1:,2] - h[:(nr_jonctiuni-1), 2])
    k = nr_jonctiuni - k_max # k -> nr clustere pt partitia optima
    return h, k

def plot_ierarhie(h, etichete, threshold, titlu="Plot ierarhie"):
    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu)
    dendrogram(h, labels=etichete, color_threshold=threshold, ax=ax)

def calcul_partitie(x, k, metoda="complete"):
    hclust = AgglomerativeClustering(k, linkage=metoda, compute_distances=True)
    hclust.fit(x) # fit() -> implementeaza modelul
    distante = hclust.distances_
    nr_jonctiuni = len(distante)
    j = nr_jonctiuni - k # j -> jonctiunea care da partitia curenta
    threshold = (distante[j] + distante[j+1]) / 2 # threshold -> medie aritmetica intre distante
    coduri = hclust.labels_ # coduri -> index pentru clusteri
    return np.array(["c"+str(cod+1) for cod in coduri]), threshold

def histograma(z, p, variabila):
    fig = plt.figure(figsize=(9,6))
    fig.suptitle("Histograme pentru variabila "+variabila)
    clase = np.unique(p) # clase -> etichete clusteri
    q = len(clase) # q -> nr de clusteri
    axe = fig.subplots(1, q, sharey=True)
    for i in range(q):
        axe[i].set_xlabel(clase[i])
        plt.hist(x=z[p == clase[i]], range=(min(z), max(z)), rwidth=0.9) # luam doar partitiile care apar in clase

def show():
    plt.show()
