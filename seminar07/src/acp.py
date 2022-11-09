# Analiza in componente principale
import numpy as np
import pandas as pd


class acp():
    def __init__(self, t, variabile=None):
        assert isinstance(t, pd.DataFrame)
        if variabile is None:
            self.variabile = list(t)
        else:
            self.variabile = variabile
        # matricea de observatii
        self.__x = t[variabile].values

    def fit(self, std=True, nlib=0, procent_varmin=80):
        n,m = self.__x.shape    # n -> nr vb., m-> nr observatii
        # centrarea datelor
        x_ = self.__x - np.mean(self.__x, axis=0)
        if std:
            # standardizarea datelor
            # standardizam daca datele sunt neomogene
            x_ = x_ / np.std(self.__x, axis=0)
        r_v = (1 / (n - nlib)) * x_.T @ x_ # @ -> operator inmultire matriceala
        # vecp -> vectorii proprii, valp -> valorile proprii -> reprezinta variantele componentelor
        valp, vecp = np.linalg.eig(r_v)
        # urmeaza sa ordonam descrescator valp si vecp
        # calculam vect de sortare
        k = np.flip(np.argsort(valp)) # sortare DEScrescatoare
        self.__alpha = valp[k]
        self.__a = vecp[:, k] # liniile nu se schimba, mutam doar coloanele
        self.__c = x_ @ self.__a

    @property
    def alpha(self):
        return self.__alpha