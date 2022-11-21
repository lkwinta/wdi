def czy_parzyste(n : int):
    while n != 0:
        if n % 2 == 0:
            return True

        n //= 10
    
    return False

def sprawdz_tablice(t, N : int):
    for i in range(N): #wiersze
        wiersz_ok = True
        
        for j in range(N): # kolumny
            if czy_parzyste(t[i][j]) == False:
                wiersz_ok = False
                break
        
        if wiersz_ok == False:
            return False

    return True

n = int(input("Rozmiar: "))
t = [[int(input()) for _ in range(n)] for _ in range(n)]

print(sprawdz_tablice(t, n))