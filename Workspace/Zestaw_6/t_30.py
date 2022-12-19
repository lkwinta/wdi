def policz_srodek_ciezkosci(punkty):
    return 0

def rekurencja(T, r, n, punkty = [], zebrano = 0, index = 0):
    if index == len(T):
        return False
    if zebrano == n:
        if policz_srodek_ciezkosci(punkty) < r:
            return True
    
    punkty.append(T[index])
    if rekurencja(T, r, n, punkty, zebrano + 1, index + 1):
        return True
    else:
        punkty.pop(len(punkty) - 1)
        return rekurencja(T, r, n, punkty, zebrano, index + 1)
    
    

def sprawdz(T, r, k):
    for i in range(3, k, 3):
        rekurencja(T, r, i)