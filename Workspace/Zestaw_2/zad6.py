from math import isqrt

n = int(input("Podaj liczbę: "))

for i in range(isqrt(n), 0, -1):
    if n%i == 0:
        print(f"{n} = {i}*{n//i}")
        break