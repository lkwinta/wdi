
def suma_szachow(T, N : int) -> int:
    licznik = 0
    for i in range(N):
        for j in range(N):
            if T[i][j] > 0:
                licznik += 1
    return licznik

def szachuj(S, N, i, j, val):
    S[i][j] += val
    if i - 1 >= 0 and j - 2 >= 0:
        S[i - 1][j - 2] += val
    if i + 1 < N and j - 2 >= 0:
        S[i + 1][j - 2] += val
    if i - 1 >= 0 and j + 2 < N:
        S[i - 1][j + 2] += val
    if i + 1 < N and j + 2 < N:
        S[i + 1][j + 2] += val

    if i - 2 >= 0 and j - 1 >= 0:
        S[i - 2][j - 1] += val
    if i + 2 < N and j - 1 >= 0:
        S[i + 2][j - 1] += val
    if i - 2 >= 0 and j + 1 < N:
        S[i - 2][j + 1] += val
    if i + 2 < N and j + 1 < N:
        S[i + 2][j + 1] += val

def usun(T, N : int) -> int:
    szachownica = [[0 for _ in range(N)] for _ in range(N)]

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in szachownica]))

    maks_suma = suma_szachow(szachownica, N)
    maks_delta = 0
    print(maks_suma)

    for i in range(len(T)):
        szachuj(szachownica, N, T[i][1], T[i][0], -1)
        x = suma_szachow(szachownica, N)
        szachuj(szachownica, N, T[i][1], T[i][0], 1)
        if maks_suma - x > maks_delta:
            maks_delta = maks_suma - x

    return maks_delta

T1 = [(1, 1), (2,3 ), (4,1), (4,5)]
T2 = [(1, 0), (2,3 ), (4,1), (4,5)]
T3 = [(5, 5)]

print(usun(T2, 10))