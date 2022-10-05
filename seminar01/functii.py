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
