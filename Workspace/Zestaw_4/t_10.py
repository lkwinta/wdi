def sprawdz_0(T, N : int):
    kolumny = [False for _ in range(N)]
    wiersze = [False for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if T[i][j] == 0:
                kolumny[j] = True
                wiersze[i] = True
    
    for i in range(N):
        if not (kolumny[i] and wiersze[i]):
            return False

    return True

n = int(input("Rozmiar: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]

print(sprawdz_0(t1, n))