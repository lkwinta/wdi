from math import isqrt

def suma_cyfr(n : int):
    suma = 0
    while n != 0:
        suma += n%10
        n //= 10

    return suma

def suma_czynnikow(n : int):
    suma = 0
    sq = isqrt(n)
    i = 2
    while n != 1:
        if n%i == 0:
            suma += suma_cyfr(i)
            n //= i
        else:
            i += 1
            if i > sq and suma == 0:
                break

       

    return suma

def liczby_smitha():
    for i in range(1, 1000000):
        if suma_cyfr(i) == suma_czynnikow(i):
            print(i)

liczby_smitha()
#print(suma_czynnikow(4))