def ilosc_cyfr(n : int):
    licznik = 0
    while n != 0:
        licznik += 1
        n //= 10
    
    return licznik

def czy_palindrom(n : int):
    liczba_cyfr = ilosc_cyfr(n)
    x = liczba_cyfr
    if x % 2 != 0:
        x -= 1

    for i in range(0, x//2):
        pierwsza_cyfra = n//10**(liczba_cyfr-1)
        if  pierwsza_cyfra != n % 10:
            return False
        
        n -= pierwsza_cyfra * 10**(liczba_cyfr-1)
        n //= 10
        liczba_cyfr -= 2

    return True

n = int(input("liczba naturalna: "))
print(czy_palindrom(n))