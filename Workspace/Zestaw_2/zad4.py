def czy_dwu_trzy_piatkowa(n : int):
    if n == 1:
        return True

    while n != 1:
        if n%2 == 0:
            n //= 2
        elif n%3 == 0:
            n //= 3
        elif n%5 == 0:
            n //= 5
        else:
            return False

    return True

n = int(input("N: "))
licznik = 0

for i in range(1, n + 1):
    licznik += czy_dwu_trzy_piatkowa(i)

print(licznik)