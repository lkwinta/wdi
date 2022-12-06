def suma(t) -> int:
    s = 0
    for i in t:
        s += i
    return s

def podzbiory(T, k, zbior1 = [], zbior2 = [], index = 0):
    if k >= len(T):
        return False
    if len(zbior1) + len(zbior2) > k:
        return False

    if len(zbior1) + len(zbior2) == k and suma(zbior1) == suma(zbior2):
        return True

    if index + 1 < len(T):
        zbior1.append(T[index])
        if podzbiory(T, k, zbior1, zbior2, index + 1):
            return True

        zbior1.pop()
        zbior2.append(T[index])
        if podzbiory(T, k, zbior1, zbior2, index + 1):
            return True

        zbior2.pop()
        if podzbiory(T, k, zbior1, zbior2, index + 1):
            return True

        return False
    

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 8
print(podzbiory(T, k))
