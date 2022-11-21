def suma_szach(T, N : int, x : int, y : int) -> int:
    suma = 0
    for i in range(N):
        if i != x:
            suma += T[x][i]
        if i != y:
            suma += T[i][y]
    
    return suma

def szachujmaks(T, N : int):
    maks = 0
    #wieża 1
    for i_1 in range(N):
        for j_1 in range(N):
            #wieża 2
            for i_2 in range(N):
                for j_2 in range(N):
                    if i_1 != i_2 and j_1 != j_2:
                        s = suma_szach(T, N, i_1, j_1) + suma_szach(T, N, i_2, j_2)
                        if s > maks:
                            maks = s