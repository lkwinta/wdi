import math

def suma_dzielnikow(n : int):
    sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            sum += i + n//i
    
    return sum

def liczby_zaprzyjaznione():
    for n in range(1, 1000000):
        a = suma_dzielnikow(n)
        if a == n or a < n:
            continue
        if suma_dzielnikow(a) == n:
            print(f"{n} , {a}")

liczby_zaprzyjaznione()