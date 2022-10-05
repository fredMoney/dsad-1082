import math


def calcul_maxim(tabel, nume_variabile):
    assert isinstance(tabel, dict)
    valori_maxime = []
    for tara in tabel.keys():
        maxim = max(tabel[tara])
        valori_maxime.append(nume_variabile[tabel[tara].index(maxim)])
    return valori_maxime

def calcul_indicatori(tabel, nlib=0):
    assert isinstance(tabel, dict)
    indicatori = []
    for v in tabel.keys():
        x = tabel[v]
        n = len(x)
        media = sum(x)/n
        std = 0
        for v_ in x:
            std += (v_ - media) ** 2
        std = math.sqrt(std / (n - nlib))
        cvar = std / media
        indicatori.append( (media, std, cvar) )
    return indicatori

def filtru(x): # x = element din tabel
    return x[1][4] > 10

def criteriu_sortare(x):
    return x[1][4]

def criteriu_sortare_lambda(x, *k): # echivalent cu criteriu_sortare_lambda(x, a, b, c, d, e...)
    return x[1][k[0]]
# *k = tuplu
# **p = dictionar; f(**p) == f(a=100, b=v...)

# selecteaza din x valorile cu cheile in *k
def selector(x, *k):
    valori_selectate = []
    for i in k[0]:
        valori_selectate.append(x[i])
    return valori_selectate
#
# def salvare(nume_fisier="output.csv"):
#
