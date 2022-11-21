def granica_iloraz(a, b, n):
    pierwszy = a
    drugi = b
    obecny = pierwszy + drugi

    for i in range(1, n):
        print(obecny/drugi)

        pierwszy = drugi
        drugi = obecny
        obecny = pierwszy + drugi

granica_iloraz(1, 1, 100)