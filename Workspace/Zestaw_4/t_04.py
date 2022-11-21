def iloraz(t, x : int, y : int, N : int):
    suma_kolumny = 0
    suma_wiersza = 0

    for i in range(N):
        suma_wiersza += t[x][i]
        suma_kolumny += t[i][y]

    return suma_kolumny / suma_wiersza

def sprawdz(t, N : int):
    maks = iloraz(t, 0, 0, N)
    x = 0
    y = 0

    for i in range(N):
        for j in range(N):
            a = iloraz(t, i, j, N)
            if a > maks: 
                maks = a
                x = i
                y = j

    return (x, y)

n = int(input("Rozmiar: "))
t = [[int(input()) for _ in range(n)] for _ in range(n)]

print(t)
print(sprawdz(t, n))