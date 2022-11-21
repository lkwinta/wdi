def czy_wielokrotnosc(x : int):
    an = 3
    n = 1
    while an <= x:
        if x % an == 0:
            return True
        n += 1
        an = n*n + n + 1

    return False

x = int(input("Podaj liczbe "))

print(czy_wielokrotnosc(x))

    