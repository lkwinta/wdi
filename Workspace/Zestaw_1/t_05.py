#newton raphson:
epsilon = float(input("Podaj dokładność: "))
n = float(input("Podaj liczbę: "))

a = 1.0
b = n

while abs(a-b) >= epsilon:
    a = (a+b)/2.0
    b = n / a

print((a+b)/2)
    