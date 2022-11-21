from math import sqrt

def ciag(n : int):
    wyraz = sqrt(0.5)
    wynik = wyraz

    for i in range(1, n):
        wyraz = sqrt(0.5 + 0.5*wyraz)
        wynik *= wyraz

    return wynik

print(2/ciag(1000000))