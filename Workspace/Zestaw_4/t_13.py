from math import isqrt

def czy_pierwsza(n : int):
    if n < 2:
        return False
    
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    
    return True

def czy_ma_komplementarna(T, N : int, a):
    for i in range(N):
        for j in range(N):
            if T[i][j] != a:
                if czy_pierwsza(T[i][j]+a):
                    return True

    return False

def sprawdz_T(T, N : int):
    for i in range(N):
        for j in range(N):
            if not czy_ma_komplementarna(T, N, T[i][j]):
                T[i][j] = 0
                
