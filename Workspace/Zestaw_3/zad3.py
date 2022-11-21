from math import isqrt

def sito(n):
    sito = [True for i in range(n+1)]
    
    sito[0] = False
    sito[1] = False

    for i in range(2, isqrt(n)+1):
        for j in range(i*i, n+1, i):
            if sito[j]:
                sito[j] = False
    
    for i in range(0, n+1):
        if sito[i]:
            print(i)

sito(int(input("Podaj max liczbe: ")))