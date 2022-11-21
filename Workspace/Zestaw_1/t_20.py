from math import sqrt

def srednia_aryt_geo(a : float, b : float):
    an = sqrt(a*b)
    bn = (a + b)/2.0

    for i in range(0, 1000):
        a = an
        b = bn

        an = sqrt(a*b)
        bn = (a + b)/2.0

    return an


print(srednia_aryt_geo(float(input("A: ")), float(input("B: "))))