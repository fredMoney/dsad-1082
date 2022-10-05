from functii import *
fisier = open(".\data\FreeLancerT.csv")

linii = fisier.readlines()
# print(linii)
fisier.close()

# Cerinta 1
print("Cerinta 1")
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
print("\nCerinta 2")
tabel2 = [v for v in zip(nume_instante,calcul_maxim(tabel,nume_variabile))]
for v in tabel2:
    print(v)

# Cerinta 3
print("\nCerinta 3")
tabel3 = [v for v in zip(nume_variabile, calcul_indicatori(tabel_))]
for v in tabel3:
    print(v)

# Cerinta 4
print("\nCerinta 4")
tabel4 = [v for v in filter(filtru, zip(nume_instante, tabel.values()))]
for v in tabel4:
    print(v[0])

# Cerinta 5
print("\nCerinta 5")
tabel5 = sorted(zip(nume_instante, tabel.values()), key=criteriu_sortare,
                reverse=True)
for v in tabel5:
    print(v)

# Cerinta 5 lambda
print("\nCerinta 5 lambda")
variabila_sortare = "C"
k = nume_variabile.index(variabila_sortare)
tabel5_ = sorted(zip(nume_instante, tabel.values()),
                 key=lambda x: criteriu_sortare_lambda(x, k),
                 reverse=True)
for v in tabel5_:
    print(v)

# Cerinta 6
print("\nCerinta 6")
variabile_selectate = ["C", "C_Test", "Java", "Java_test"]
j = [] # j = lista indecsi
for v in variabile_selectate:
    j.append(nume_variabile.index(v))
tabel6 = [v for v in zip(nume_instante, map(lambda x:selector(x, j), tabel.values()))]
for v in tabel6:
    print(v)
