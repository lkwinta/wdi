def e(eps : float):
    mnoznik = 1
    wynik = 1
    wyraz = 1

    while wyraz > eps:
        wyraz = wyraz/mnoznik
        wynik += wyraz
        mnoznik += 1

    return wynik

print(e(0.001))