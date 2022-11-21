def kwadrat(t, N : int, k : int):
    if N < 3:
        print("Nie znaleziono")
        return (-1, -1)

    rozmiar = 3
    while rozmiar <= N:
        for x in range(N-rozmiar + 1):
            for y in range(N-rozmiar+1):
                lg = t[x][y]
                pg = t[x][y+rozmiar-1]
                pd = t[x+rozmiar-1][y+rozmiar-1]
                ld = t[x+rozmiar-1][y]

                if lg*pg*pd*ld == k:
                    return (x+rozmiar//2, y+rozmiar//2)

        rozmiar += 2
    
    print("Nie znaleziono")
    return (-1, -1)

n = int(input("Rozmiar: "))
k = int(input("k: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]

print(kwadrat(t1, n, k))