import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import heatmap


def medie_ponderata(t, coloane_calcul, coloana_pondere):
    assert isinstance(t, pd.DataFrame)
    x = t[coloane_calcul].values
    w = t[coloana_pondere].values
    medii = np.average(x, axis=0, weights=w)

    return pd.Series(medii, coloane_calcul)


def graficCorelograma(r, titlu):
    fig = plt.figure(figsize=(8, 8)) # dim in inch.
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16,
                                  "color": "b"})
    heatmap(r, vmin=-1, vmax=1, cmap="RdYlBu", annot=True, ax=ax)
    plt.show()