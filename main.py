# macierz = [
#     [1,23,5,2],
#     [2,4,5,2],
#     [2,0,0,-2],
#     [2,2,-1,-1]
# ]

# macierz = [
#     [1,1,2,1,4],
#     [2,3,3,1,2],
#     [3,2,4,1,3],
#     [4,5,5,-2,3],
#     [5,4,6,1,3],
# ]


def generujMacierz():
    n = int(input('Podaj wielkosc macierzy, ktorej wyznacznik chcesz obliczyc: '))
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            wiersz.append(int(input('Podaj liczbe: ')))
        print('----------------')
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for row in macierz:
        for i in range(len(row)):
            print(f'[{row[i]}]', end=' ')
        print()
    return 0

def wyznacznik3(macierz):
    przekatneDol = 0
    przekatneGora = 0
    for kolumnaStart in range(3):
        iloraz = 1
        for i in range(3):
            wiersz = i
            kolumna = (kolumnaStart + wiersz)%3
            iloraz *= macierz[wiersz][kolumna]

        przekatneDol += iloraz

    for kolumnaStart in range(3):
        iloraz = 1
        for i in range(3):
            wiersz = 2 - i
            kolumna = (kolumnaStart + i)%3
            iloraz *= macierz[wiersz][kolumna]

        przekatneGora += iloraz

    return przekatneDol - przekatneGora

def znajdzNajwiecejZer(macierz):
    wiersze = [0]*len(macierz)
    kolumny = [0]*len(macierz)
    for i in range(len(macierz)):
        count = macierz[i].count(0)
        wiersze[i] = count
        kolumna = []
        for j in range(len(macierz[i])):
            kolumna.append(macierz[j][i])
        kolumny[i] = kolumna.count(0)

    return ('wiersz',wiersze.index(max(wiersze))) if max(wiersze) >= max(kolumny) else ('kolumna', kolumny.index(max(kolumny)))

def minor(wierszDoUsuniecia, kolumnaDoUsuniecia, macierz):
    wycietaMacierz = []
    for i in range(len(macierz)):
        wiersz = []
        if i == wierszDoUsuniecia:
            continue
        for j in range(len(macierz[i])):
            if j != kolumnaDoUsuniecia:
                wiersz.append(macierz[i][j])
        wycietaMacierz.append(wiersz)
    return wycietaMacierz

def metodaLaplace(macierz):
    if len(macierz) == 2:
        return f'({macierz[0][0]} * {macierz[1][1]}) - ({macierz[0][1]} * {macierz[1][0]}) = {(macierz[0][0] * macierz[1][1]) - (macierz[0][1] * macierz[1][0])}'
    if len(macierz) == 3:
        return wyznacznik3(macierz)
    krotka = znajdzNajwiecejZer(macierz)
    det = 0
    i = krotka[1]
    if krotka[0] == 'wiersz':
        for j in range(len(macierz[i])):
            if macierz[i][j] == 0:
                continue
            if len(minor(i, j, macierz)) > 3:
                wyznacznik = metodaLaplace(minor(i, j, macierz))
            else:
                wyznacznik = wyznacznik3(minor(i, j, macierz))
            sign = (-1) ** (i + j)
            det += macierz[i][j] * sign * wyznacznik
    if krotka[0] == 'kolumna':
        for j in range(len(macierz[i])):
            if macierz[j][i] == 0:
                continue
            wyznacznik = wyznacznik3(minor(j, i, macierz))
            det += macierz[j][i]*((-1)**(i+j))*wyznacznik
    return det

macierz = generujMacierz()
wypisz(macierz)
print(metodaLaplace(macierz))