def sprawdz_ciag(t, x : int, y: int, N):
    maks_dlugosc = 2
    obecna_dlugosc = 2
    obecne_q = t[x+1][y+1] / t[x][y]
    x += 2
    y += 2

    while x < N and y < N:
        if t[x][y] / t[x-1][y-1] == obecne_q:
            obecna_dlugosc += 1
        else:
            if obecna_dlugosc > maks_dlugosc:
                maks_dlugosc = obecna_dlugosc

            obecna_dlugosc = 2
            obecne_q = t[x][y] / t[x-1][y-1]

        x += 1
        y += 1
    
    if obecna_dlugosc > maks_dlugosc:
        maks_dlugosc = obecna_dlugosc

    return maks_dlugosc

def ciag_geometryczny(T1, N : int):
    if N < 3:
        print("Nie znaleziono")
        return 0
    
    x = N - 3
    y = 0
    
    maks = 2

    while x >= 0 and y <= N-3:
        dlu = sprawdz_ciag(T1, x, y, N)
        if dlu > maks:
            maks = dlu

        if x > 0:
            x -= 1
        else:
            y += 1
    
    return maks


n = int(input("Rozmiar: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]
print(ciag_geometryczny(t1, n))