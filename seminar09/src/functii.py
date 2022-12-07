import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import kdeplot
from sklearn.metrics import confusion_matrix, cohen_kappa_score


def plot_distributie(z, y, k=0):    # k-> indexul axei discriminante
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Distributie in axa discriminanta "+str(k+1), fontsize=16, color="b")
    kdeplot(x=z[:,k], hue=y, fill=True, ax=ax)


def show():
    plt.show()


def calcul_metrici(y, y_, clase):    # y -> vectorul cu clase, y_ -> ???, clase -> numele claselor
    c = confusion_matrix(y, y_)
    tabel_confuzie = pd.DataFrame(c, clase, clase)
    tabel_confuzie["Acuratete"] = np.round(np.diag(c) / np.sum(c, axis=1) * 100)
    acuratete_medie = tabel_confuzie["Acuratete"].mean()
    acuratete_globala = np.round(sum(np.diag(c) * 100 / len(y)), 3)
    index_CK = cohen_kappa_score(y, y_)
    acuratete = pd.Series([acuratete_globala, acuratete_medie, index_CK],
                          ["Acuratete globala", "Acuratete medie", "Index Cohen-Kappa"],
                          name="Acuratete")
    return tabel_confuzie, acuratete