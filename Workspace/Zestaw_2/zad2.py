a = int(input("a: "))
b = int(input("b: "))
n = int(input("n: "))

print(a//b, end=",")
roznica = a - a//b*b

for i in range(0, n):
    roznica *= 10
    print(roznica//b, end="")
    roznica -= roznica//b*b

print()