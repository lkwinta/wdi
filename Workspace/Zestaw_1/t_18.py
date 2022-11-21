#newton raphson:
epsilon = float(input("Podaj dokładność: "))
n = float(input("Podaj liczbę: "))

a = 1
b = n

while abs(a - b) > epsilon:
    a = (a + b)/2
    b = n / (a*a)

print(a)