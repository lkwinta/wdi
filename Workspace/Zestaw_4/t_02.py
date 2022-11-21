def czy_nieparzyste(n : int):
    while n != 0:
        if n % 2 == 0:
            return False

        n //= 10
    
    return True

def sprawdz_tablice(t, N : int):
    for i in range(N): #wiersze
        wiersz_ok = False
        
        for j in range(N): # kolumny
            if  czy_nieparzyste(t[i][j]) == True:
                wiersz_ok = True
                break
        
        if wiersz_ok != True:
            return False

    return True

n = int(input("Rozmiar: "))
t = [[int(input()) for _ in range(n)] for _ in range(n)]

print(sprawdz_tablice(t, n))