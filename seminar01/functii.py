def calcul_maxim(tabel, nume_variabile):
    assert isinstance(tabel, dict)
    valori_maxime = []
    for tara in tabel.keys():
        maxim = max(tabel[tara])
        valori_maxime.append(nume_variabile[tabel[tara].index(maxim)])
    return valori_maxime

