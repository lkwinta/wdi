def pole(T, N, w, k, n):
    if 0 <= w < N and 0 <= k < N:
        T[w][k] += n

def szachuj(T, N, w, k, n):
    pola = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for (i, j) in pola:
        pole(T, N, w + i, k + j, n)

def sumuj(T, N):
    suma = 0
    for w in range(N):
        for k in range(N):
            suma += (T[w][k] > 0)
    return suma

def place(T):
    N = len(T) 
    for w in range(N):
        for k in range(N):
            if T[w][k] == 1:
                szachuj(T, N, w, k, 1)

    poz = (0, 0)
    min_odleglosc = 2 * N
    maks_roznica = 0

    suma_0 = sumuj(T, N)

    for w in range(N):
        for k in range(N):
            if T[w][k] == 0:
                szachuj(T, N, w, k, 1)
                suma_1 = sumuj(T, N)
                if suma_1 - suma_0 > maks_roznica:
                    maks_roznica = suma_1 - suma_0
                    poz = (w, k)
                    min_odleglosc = max(abs(w - N//2), abs(k - N//2))
                elif suma_1 - suma_0 == maks_roznica:
                    odleglosc = max(abs(w - N//2), abs(k - N//2))
                    if odleglosc < min_odleglosc:
                        min_odleglosc = odleglosc
                        poz = (w, k)
                szachuj(T, N, w, k, -1)

    return poz