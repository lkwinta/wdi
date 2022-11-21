def czy_ciag_rosnacy(n : int):
    ostatnia_cyfra = n%10
    n //= 10

    while n != 0:
        if n%10 >= ostatnia_cyfra:
            return False
        ostatnia_cyfra = n%10
        n //= 10

    return True

n = int(input("Podaj liczbe: "))
print(czy_ciag_rosnacy(n))