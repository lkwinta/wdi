import math
from re import I

def suma_dzielnikow(n : int):
    sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            sum += i + n//i
    
    return sum

def liczby_doskonale():
    for n in range(2, 1000000):
        if suma_dzielnikow(n) == n:
            print(n)

liczby_doskonale()