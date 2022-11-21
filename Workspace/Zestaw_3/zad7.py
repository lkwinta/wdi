from random import randint

def czy_nieparzysta(n : int) -> bool:
    while n != 0:
        if n%2 != 0:
            return True
        n //= 10

    return False

def sprawdz_tablice(t, N : int) -> bool:
    for i in range(N):
        if czy_nieparzysta(int(t[i])) != True:
            return False
    
    return True

def zad7():
    n = int(input("podaj ilosc: "))
    t = [randint(1, 1000) for _ in range(n)]
    print(sprawdz_tablice(t, n))

zad7()