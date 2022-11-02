import pandas as pd
import numpy as np
from functii import medie_ponderata, graficCorelograma

industria_a = pd.read_csv("..\\data\\IndustriaAlimentara.csv", index_col=0)
populatie = pd.read_csv("..\\data\\PopulatieLocalitati.csv", index_col=0)

activitati = list(industria_a)[1:]
# print(activitati)

# Cerinta 1
t_cerinta1 = industria_a[industria_a[activitati].sum(axis=1) > 0]
t_cerinta1.to_csv("..\\data\\Cerinta1.csv")


# Cerinta 2
industria_a_ = industria_a[activitati]\
    .merge(populatie[["Judet","Populatie"]], left_index=True, right_index=True)
t_cerinta2 = industria_a_.groupby(by="Judet")\
    .apply(func=medie_ponderata, coloane_calcul=activitati, coloana_pondere = "Populatie")
t_cerinta2.to_csv("..\\data\\Cerinta2.csv")

# Cerinta 3
industria_a_judete = industria_a_.groupby(by="Judet").agg(sum)
# print(industria_a_judete)
x = industria_a_judete[activitati].values # x -> nr. de muncitori
p = industria_a_judete["Populatie"].values # p -> populatie
p_x = x / np.sum(x, axis=0) # p_x -> %muncitori pe judet
p_ = p / sum(p) # p_ -> %locuitori judet din total
l = (p_x.T / p_).T # l -> indicii de localizare
t_cerinta3 = pd.DataFrame(l, industria_a_judete.index, activitati)
t_cerinta3.to_csv("..\\data\\Cerinta3.csv")


# Cerinta 4
graficCorelograma(t_cerinta3.corr(), "Corelograma pe indicii de localizare")


# TODO:
# Cerinta 5
