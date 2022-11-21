def ilosc_cyfr(n : int):
    licznik = 0
    while n != 0:
        licznik += 1
        n //= 10
    
    return licznik

def czy_cyfra_ilosc_cyfr(n : int):
    cyfry = ilosc_cyfr(n)
    while n != 0:
        if n%10 == cyfry:
            return True
        
        n //= 10

    return False

n = int(input("Podaj liczbe: "))
print(czy_cyfra_ilosc_cyfr(n))