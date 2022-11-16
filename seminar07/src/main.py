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
show()