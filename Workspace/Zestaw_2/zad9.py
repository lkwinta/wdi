def f(x : float):
    return 1/x

def prostokaty(k : float, delta : float):
    x = 1
    wynik = 0

    while x <= k:
        wynik += f(x+delta/2)*delta
        x += delta

    return wynik

k = float(input("Podaj k: "))
delta = float(input("Podaj delta: "))
print(prostokaty(k, delta))