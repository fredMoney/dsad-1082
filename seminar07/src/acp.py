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
        x_ = self.__x - np.mean(self.__x, axis=0) # x_ -> tabel de date centrate
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

        # Criterii de relevanta -> cate componente sunt semnificative
        # 1. Procentul minimal (% Varianta cumulata)
        p_var_cum = np.cumsum(self.__alpha) * 100 / sum(self.alpha)
        # np.where() returneaza tuplu de vectori
        k1 = np.where(p_var_cum > procent_varmin)[0][0]  # filtrare -> filtram comps. cu var_cum > 80

        # 2. Kaiser
        if std:
            k2 = np.where(self.alpha < 1)[0][0] - 1  # intorace false pana la comp. 7 -> -1 => comp. 6
        else:
            k2 = None

        # 3. Cattel (google)
        # m -> nr. de observatii
        eps = self.alpha[:(m - 1)] - self.alpha[1:]  # eps -> diferentele intre observatii
        d = eps[:(m - 2)] - eps[1:]  # mai scadem o data -> pozitia cautata e primul negativ + 1
        negative = d < 0
        if any(negative):
            k3 = np.where(negative)[0][0] + 1
        else:
            k3 = None

        self.__criterii = (k1, k2, k3)

        # Calcul corelatii
        if std:
            self.__r = self.__a*np.sqrt(self.__alpha)
        else:
            self.__r= np.where(self.x_, self.__c, rowvar=False)[:m, m:] # rowvar=False -> datele sunt pe coloane


    @property
    def alpha(self):
        return self.__alpha

    @property
    def a(self):
        return self.__a

    @property
    def c(self):
        return self.__c

    @property
    def r(self):
        return self.__r

    @property
    def criterii(self):
        return self.__criterii
