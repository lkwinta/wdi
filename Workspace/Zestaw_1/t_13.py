def nwd(a : int, b : int):
    while b != 0:
        c = a % b
        a = b
        b = c
    
    return a

def nww(a : int, b : int):
    return a*b//nwd(a,b)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ab = nww(a, b)
abc = nww(ab, c)

print(abc)