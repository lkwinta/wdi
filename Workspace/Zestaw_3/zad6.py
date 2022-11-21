def czy_nieparzysta(n : int) -> bool:
    while n != 0:
        if n%2 != 0:
            return True
        n //= 10

    return False

def sprawdz_tablice(t, N : int) -> bool:
    for i in range(N):
        if czy_nieparzysta(t[i]) != True:
            return False
    
    return True

def zad6():
    n = int(input("Ilosc elementow: "))
    t = [int(input("Podaj kolejna liczbe: ")) for _ in range(n)]
    print(type(t))
    print(sprawdz_tablice(t, n))

zad6()
