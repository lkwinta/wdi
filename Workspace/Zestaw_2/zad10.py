def czy_wielokrotnosc(n : int):
    a1 = 2
    while a1 <= n:
        if n%a1 == 0:
            return True

        a1 = 3*a1 + 1

    return False 

print(czy_wielokrotnosc(int(input("Podaj liczbę: "))))       