def czy_ostatnia_unikalna(n : int):
    ostatnia_cyfra = n%10
    n //= 10

    while n != 0:
        if n%10 == ostatnia_cyfra:
            return False
        n//=10

    return True

n = int(input("Podaj liczbę: "))
print(czy_ostatnia_unikalna(n))