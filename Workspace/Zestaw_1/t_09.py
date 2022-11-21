import math

def dzielniki(n : int):
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            print(f"{i} {n//i}")

dzielniki(12)