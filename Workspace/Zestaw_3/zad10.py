def najdluzszy_podciag_arytmetyczny(t, N : int) -> int:
    maks_dlugosc = 2
    obecna_dlugosc = 2
    obecne_r = t[1] - t[0]

    for i in range(2, N):
        if t[i] - t[i-1] == obecne_r:
            obecna_dlugosc += 1
        else:
            if obecna_dlugosc > maks_dlugosc:
                maks_dlugosc = obecna_dlugosc
            
            obecne_r = t[i] - t[i - 1]
            obecna_dlugosc = 2

    if obecna_dlugosc > maks_dlugosc:
        maks_dlugosc = obecna_dlugosc

    return maks_dlugosc

n = int(input("Ilosc elementow: "))
t = [int(input()) for _ in range(n)]

print(najdluzszy_podciag_arytmetyczny(t, n))