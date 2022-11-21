from math import log10

def wytnij(n : int, maska : int):
    wynik = 0
    i = 0
    while n != 0:
        if maska % 2 == 1:
            wynik += n%10 * 10**i
            i += 1

        maska //= 2
        n //= 10
    
    return wynik


def podzielnosc(n : int, dzielnik : int):
    ilosc_cyfr = int(log10(n)) + 1
    licznik = 0
    for i in range(2**ilosc_cyfr-1):
        
        x = wytnij(n, i)
        if x % dzielnik == 0:
            licznik += 1
            #print(x, bin(i).replace("0b",""))

    return licznik

print(podzielnosc(int(input("Podaj liczbe: " )), 7))