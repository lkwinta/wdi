from math import isqrt

def czy_pierwsza(n : int):
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

a = int(input("Liczba 1: "))
b = int(input("Liczba 2: "))