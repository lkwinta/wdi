def ciag(an : float):
    i = 0
    while an != 1:
        an = (an % 2) * (3 * an + 1) + (1 - an % 2) * (an / 2)
        i += 1
    
    return i

maks = 0
maks_wartosc = -1

for i in range(2, 10000+1):
    x = ciag(i)
    if(x > maks):
        maks = x
        maks_wartosc = i

print(f"{maks_wartosc} po {maks} krokach")