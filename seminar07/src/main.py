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
