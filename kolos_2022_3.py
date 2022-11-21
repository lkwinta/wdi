def nwd(a : int, b : int):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a

def trojki(T):
    for i in range(len(T)):
        for j in range(len(T)):
            a = 0

print(nwd(4, 12))