def f(x):
    return x**x - 2020

def bisekcja(epsilon):
    lewy = 4.0
    prawy = 5.0
    while abs(f((lewy + prawy)/2)) > epsilon:
        if f((lewy + prawy)/2) > 0:
            prawy = (lewy + prawy)/2
        else:
            lewy = (lewy + prawy)/2

    return (lewy + prawy)/2

epsilon = float(input("Podaj dokładność: "))
print(bisekcja(epsilon))