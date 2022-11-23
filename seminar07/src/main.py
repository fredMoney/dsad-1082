import numpy as np

from functii import *
from acp import *
import pandas as pd

# indexul este Indicativ judet
tabel = pd.read_csv("..//data//Teritorial.csv", index_col=1)
nan_replace_t(tabel)
variabile = list(tabel)[3:]

model_acp = acp(tabel, variabile)
model_acp.fit()
# print("Varianta componente:", model_acp.alpha, sum(model_acp.alpha))

tabel_varianta = tabelare_varianta(model_acp.alpha)
tabel_varianta.to_csv("..//data//varianta.csv")

criterii = model_acp.criterii
alpha = model_acp.alpha
plot_varianta(alpha, criterii)

r = model_acp.r
etichete = ["C"+str(i+1) for i in range(len(variabile))]
t_r = pd.DataFrame(r, index=variabile, columns=etichete)
corelograma(t_r)

c = model_acp.c
t_c = pd.DataFrame(c, tabel.index, etichete)
k = min([v for v in criterii if v is not None]) + 1 # k -> nr de comps. semnificative
print(k)

plot_instante(t_c)

# Calculul cosinusuri
c2= c*c
cosin = (c2.T/np.sum(c2, axis=1)).T
pd.DataFrame(cosin, t_c.index, t_c.columns).to_csv("..//data//cosin.csv")

# Calcul contributii
q = c2/np.sum(c2, axis=0)
pd.DataFrame(q,t_c.index, t_c.columns).to_csv("..//data//q.csv")

# Comunalitati
r2 = r*r
comm = np.cumsum(r2, axis=1)
t_comm = pd.DataFrame(comm,t_r.index, t_r.columns)
t_comm.to_csv("..//data//comm.csv")
corelograma(t_comm, 0, titlu="Comunalitati")

show()