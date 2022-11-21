n = int(input("Podaj n^2: "))

suma = 0
nastepny = 1
x = 0 # ilosc elementow

while suma < n:
    suma += nastepny
    x += 1
    nastepny += 2

if suma == n:
    ostatni = 1 + 2*(x-1)
    wynik = int((1 + ostatni)/2)
    print(wynik)
else:
    print("Brak pierwiastka")
