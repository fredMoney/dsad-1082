import numpy as np

from functii import *
from acp import *
import pandas as pd
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo

tabel = pd.read_csv("..//data//Teritorial.csv", index_col=1)
nan_replace_t(tabel)
variabile = list(tabel)[3:]

# Evaluare factorabilitate
x = tabel[variabile].values
test_bartlet = calculate_bartlett_sphericity(x)
print("Test Barlett:", test_bartlet)
if test_bartlet[1] > 0.01:
    print("Nu exista factori!")
    exit(0)

kmo = calculate_kmo(x)
t_kmo = pd.DataFrame(
    data={
        "Index KMO":np.append(kmo[0], kmo[1])
    }, index=[variabile+["Total"]]
)
t_kmo.to_csv("..//data//t_kmo.csv")
print(t_kmo)
corelograma(t_kmo, 0, titlu="Index KMO")

# Construire model
q = len(variabile)
# model_af = FactorAnalyzer(n_factors=q, rotation="varimax") varimax -> roteste axele
model_af = FactorAnalyzer(n_factors=q, rotation=None)
model_af.fit(x)

# Preluare rezultate si analiza
varianta_factori = model_af.get_factor_variance()
# print(varianta_factori)
etichete_factori = ["F"+str(i+1) for i in range(q)]
tabel_varianta = pd.DataFrame(
    data={
        "Varianta":varianta_factori[0],
        "Procent varianta":varianta_factori[1]*100,
        "Procent cumulat":varianta_factori[2]*100
    }, index=etichete_factori
)
# print(tabel_varianta)
tabel_varianta.to_csv("..//data//Varianta_f.csv")

# Corelatii variabile-factori
# X = F @ L.T + e
# o vb. L reprezinta corelatia dintre X si F
l = model_af.loadings_
t_l = pd.DataFrame(l, variabile, etichete_factori)
t_l.to_csv("..//data//l.csv")
corelograma(t_l, titlu="Corelatii variabile-factori")

show()