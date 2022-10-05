from functii import *
fisier = open(".\data\FreeLancerT.csv")

linii = fisier.readlines()
# print(linii)
fisier.close()

# Cerinta 1
linie_variabile = linii[0][:-1].split(",")
# print(linie_variabile)
nume_index = linie_variabile[0]
tabel = {}
tabel_ = {}
for v in linie_variabile[3:]:
    tabel_[v] = []
# print(tabel,tabel_,sep="\n")
for i in range(1, len(linii)):
    linie = linii[i][:-1].split(",")
    tabel[linie[0]] = [float(v) for v in linie[3:]]
    for j in range(3, len(linie)):
        tabel_[linie_variabile[j]].append(float(linie[j]))
# print(tabel, tabel_, sep="\n")
for tehnologie in tabel_.keys():
    print(tehnologie,tabel_[tehnologie])
nume_instante = list(tabel.keys())
nume_variabile = list(tabel_.keys())
# print(nume_variabile,type(nume_variabile),sep="\n")

# Cerinta 2
tabel2 = [v for v in zip(nume_instante,calcul_maxim(tabel,nume_variabile))]
for v in tabel2:
    print(v)

# Cerinta 3

