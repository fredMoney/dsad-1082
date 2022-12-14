import pandas as pd
from functii import *

tabel_date = pd.read_csv("..//res//Teritorial.csv", index_col=1) # -> "Indicativ" (coloana 1) e index
nan_replace_t(tabel_date)

variabile = list(tabel_date)[3:] # -> se preiau numele coloanelor
x = tabel_date[variabile].values # x -> matricea de observatii

h, k_opt = calcul_ierarhie(x)
# plot_ierarhie(h, tabel_date.index, max(h[:,2])+1)
# show()

# Creare partitie optima
p_opt = calcul_partitie(x, k_opt)
# plot_ierarhie(h, tabel_date.index, p_opt[1], "Plot partitie optimala")
# print(p_opt[0])
# show()

# Creare partitie din 3 clusteri
p3 = calcul_partitie(x, 3)
# plot_ierarhie(h, tabel_date.index, p3[1], "Plot 3 partitii")
print(p3[0])

# Desenare histograme
for i in range(len(variabile)):
    histograma(x[:,i], p3[0], variabile[i])
show()

tabel_partitii = pd.DateFrame(
    data = {
        "Popt": p_opt[0],
        "P3": p3[0]
    }, index=tabel_date.index
)

print(tabel_partitii)
tabel_partitii.to_csv("..//res//partitii.csv")