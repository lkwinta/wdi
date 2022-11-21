def nwd(a : int, b : int):
    while b != 0:
        c = a % b
        a = b
        b = c
    
    return a

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(nwd(a, nwd(b, c)))