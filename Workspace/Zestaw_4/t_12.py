from math import isqrt

def czy_zlozona(n : int):
    if n <= 2:
        return False
    
    for i in range(2, isqrt(n) + 1):
        if n%i == 0:
            return True
    
    return False

def sprawdz_T(T, N : int):
    poprzedni_poziom = -1

    for poziom in range(N):
        licznik = 0
        for i in range(N):
            for j in range(N):
                ile_sasiadow = 0

                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if ( 0 <= i + x <= N-1 and
                             0 <= i + y <= N-1 and
                             not (x == 0 and y == 0)):
                            ile_sasiadow += czy_zlozona(T[i+x][i+y])
                
                if ile_sasiadow >= 6:
                    licznik += 1
        
        if poprzedni_poziom == -1:
            poprzedni_poziom = licznik
        else:
            if poprzedni_poziom != licznik:
                return False
    
    return True

n = int(input("Rozmiar: "))
t1 = [[[int(input()) for _ in range(n)] for _ in range(n)] for _ in range(n)]

print(sprawdz_T(t1, n))