def czy_przyjaciolki(a : int, b : int):
    cyfry = [False for _ in range(10)]
    
    while a != 0:
        cyfry[a%10] = True
        a //= 10
    
    while b != 0:
        if cyfry[b%10] == False:
            return False
        b //= 10
    
    return True

def sprawdz_T(T, N : int):
    licznik = 0
    for i in range(N):
        for j in range(N):
            licznik_obecny = 0
            licznik_max = 0

            if i > 0: 
                licznik_obecny += czy_przyjaciolki(T[i][j], T[i-1][j]) #góra
                licznik_max += 1
                if j > 0:
                    licznik_obecny += czy_przyjaciolki(T[i][j], T[i-1][j-1]) #góra-lewo
                    licznik_max += 1
                if j < N - 1:
                    licznik_obecny += czy_przyjaciolki(T[i][j], T[i-1][j+1]) #góra-prawo
                    licznik_max += 1
            if i < N - 1:
                licznik_obecny += czy_przyjaciolki(T[i][j], T[i+1][j]) #dół
                licznik_max += 1
                if j > 0:
                    licznik_obecny += czy_przyjaciolki(T[i][j], T[i+1][j-1]) #dół-lewo
                    licznik_max += 1
                if j < N - 1:
                    licznik_obecny += czy_przyjaciolki(T[i][j], T[i-1][j+1]) #dół-prawo
                    licznik_max += 1
            if j > 0:
                licznik_obecny += czy_przyjaciolki(T[i][j], T[i][j-1]) #lewo
                licznik_max += 1
            if j < N - 1:
                licznik_obecny += czy_przyjaciolki(T[i][j], T[i][j+1]) #w prawo
                licznik_max += 1

            if licznik_obecny == licznik_max:
                licznik += 1

    return licznik

n = int(input("Rozmiar: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]

print(sprawdz_T(t1, n))