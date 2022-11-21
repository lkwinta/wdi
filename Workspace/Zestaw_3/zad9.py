def najdluzszy_podciag_rosnacy(t, N : int) -> int:
    maks_dlugosc = 1
    obecna_dlugosc = 1

    for i in range(1, N):
        if t[i - 1] < t[i]:
            obecna_dlugosc += 1
        else:
            if obecna_dlugosc > maks_dlugosc:
                maks_dlugosc = obecna_dlugosc
            
            obecna_dlugosc = 0

    if obecna_dlugosc > maks_dlugosc:
        maks_dlugosc = obecna_dlugosc

    return maks_dlugosc

n = int(input("Ilosc elementow: "))
t = [input() for _ in range(n)]

print(najdluzszy_podciag_rosnacy(t, n))

