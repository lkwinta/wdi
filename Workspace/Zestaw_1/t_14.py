from cmath import pi

def cos(x : float, eps : float):
    silnia = 1
    i = 0
    wynik = 0
    wyraz = 1

    while wyraz > eps:
        wyraz = (x**i)/silnia
        wynik += ((-1)**(i/2)) * wyraz
        i += 2
        silnia = silnia * (i - 1) * i

    return wynik

print(cos(pi/4, 0.0001))
