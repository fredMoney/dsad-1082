import numpy as np
import pandas as pd
import pylab as pl
from matplotlib import pyplot as plt
from pandas.api.types import is_numeric_dtype
from seaborn import heatmap

def nan_replace_t(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

def tabelare_varianta(alpha):
    return pd.DataFrame(
        data={
            "Varianta": np.round(alpha, 3),
            "Varianta cumulata": np.round(np.cumsum(alpha), 3),
            "Procent varianta": np.round(alpha * 100 / sum(alpha), 3),
            "Procent cumulat": np.round(np.cumsum(alpha * 100 / sum(alpha)), 3)
        }, index=["Comp"+str(i+1) for i in range(len(alpha))]
    )

def plot_varianta(alpha, criterii):
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, pl.Axes)
    ax.set_title("Plot valori proprii", fontdict = {"fontsize": 16, "color": "b"})
    ax.set_xlabel("Componenta")
    ax.set_ylabel("Varianta")
    m = len(alpha)
    x = np.arange(1, m + 1)
    ax.set_xticks(x)
    ax.plot(x, alpha)
    ax.scatter(x, alpha, c="r")
    k1, k2, k3 = criterii
    ax.axvline(k1 + 1, label="Acoperire minimala", c="g")
    if k2 is not None:
        ax.axvline(k2 + 1, label="Criteriu Kaiser", c="m")
    if k3 is not None:
        ax.axvline(k3 + 1, label="Criteriu Cattel")
    ax.legend()


def corelograma(r, vmin=-1, cmap="RdYlBu", titlu="Corelatii factoriale"):
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(1, 1, 1) # ax -> obiectul axa
    ax.set_title(titlu, fontdict = {"fontsize": 16, "color": "b"})
    heatmap(r, vmin=vmin, cmap=cmap, annot=False, ax=ax)


def plot_instante(t, k1=0, k2=1, titlu="Plot instante"):
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(1, 1, 1, aspect=1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(t.columns[k1])
    ax.set_ylabel(t.columns[k2])
    ax.scatter(t.iloc[:,k1], t.iloc[:,k2], c="r")
    for i in range(len(t.index)):
        ax.text(t.iloc[i,k1], t.iloc[i,k2], t.index[i])



def show():
    plt.show()
