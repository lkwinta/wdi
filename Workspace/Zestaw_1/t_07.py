def czy_jest_iloczynem(n : int):
    if n == 1:
        return True
    
    pierwszy = 1
    drugi = 1
    obecny = pierwszy + drugi

    while obecny < liczba:
        if pierwszy*drugi == n:
            return True

        pierwszy = drugi
        drugi = obecny
        obecny = pierwszy + drugi

    if drugi * obecny == n:
        return True

    return False

liczba = int(input("Podaj liczbę: "))
print(czy_jest_iloczynem(liczba))