def czy_pierwsza(n : int):
    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    sqrtn = n**0.5

    while i <= sqrtn:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


print(czy_pierwsza(int(input("Podaj liczbę: "))))