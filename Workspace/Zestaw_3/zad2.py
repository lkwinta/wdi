def te_same_cyfr(a : int, b : int):
    zlicz = [0 for _ in range(10)]
    while a != 0:
        zlicz[a%10] += 1
        a //= 10

    while b != 0:
        if zlicz[b%10] == 0:
            return False
        else:
            zlicz[b%10] -= 1
        b //= 10
    
    for i in range(10):
        if zlicz[i] != 0:
            return False

    return True

print(te_same_cyfr(int(input("Podaj a: ")), int(input("Podaj b: "))))