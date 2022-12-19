def nwd(a : int, b : int):
    while b != 0:
        c = a%b
        a = b
        b = c
    
    return a

def rekurencja(w : int, k : int, w_koniec : int, k_koniec : int, szachownica, N : int, kierunek : int, kroki : int = 0):
    if w < N and w >= 0 and k < N and k >= 0:
        if w == w_koniec and k == k_koniec:
            return kroki
        wynik1 = float("inf")
        wynik2 = float("inf")
        for w_1 in range(w + 1, N):
            if nwd(int(szachownica[w][k]), int(szachownica[w_1][k])):
                wynik1 = min(wynik1, rekurencja(w_1, k, w_koniec, k_koniec, szachownica, N, kierunek, kroki+1))
 
        for k_1 in range(k + 1, N, kierunek):
            if nwd(int(szachownica[w][k]), int(szachownica[w][k_1])):
                wynik2 = min(wynik2, rekurencja(w, k_1, w_koniec, k_koniec, szachownica, N, kierunek, kroki+1))

        return min(wynik1, wynik2)
    else:
        return float("inf")

def funkcja(szachownica):
    w1 = rekurencja(0, 0, len(szachownica) - 1, len(szachownica) - 1, szachownica, len(szachownica), 1)
    w2 = rekurencja(0, len(szachownica) - 1, len(szachownica) - 1, 0, szachownica, len(szachownica), -1)

    if w1 == float("inf") and w2 == float("inf"):
        return 0
    else:
        if w1 > w2:
            return 2
        elif w1 < w2:
            return 1
        else:
            return 0