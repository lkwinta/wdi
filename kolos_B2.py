def unikatowe_dzielniki(n):
    licznik = 0
    dzielnik = 2

    while n != 1:
        if n % dzielnik == 0:
            licznik += 1
            n //= dzielnik
        else:
            while n % dzielnik != 0:
                dzielnik += 1
                
    return licznik

def square(T):
    for bok in range(1, len(T)):
        for i in range(len(T) - bok):
            for j in range(len(T) - bok):
                iloczyn = T[i][j] * T[i+bok][j] * T[i][j+bok] * T[i+bok][j+bok]

                if unikatowe_dzielniki(iloczyn) == 2:
                    return bok + 1
    
    return 0

n = int(input())
T = [[int(input()) for _ in range(n)] for _ in range(n)]

print(square(T))