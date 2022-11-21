from json.encoder import INFINITY

def max10():
    x = 1
    tab_maks = [0 for _ in range(10)]

    while x != 0:
        x = int(input())
        min_indeks = -1
        min_wartosc = INFINITY

        for i in range(10):
            if tab_maks[i] < min_wartosc:
                min_indeks = i
                min_wartosc = tab_maks[i]
        
        if x > min_wartosc:
            tab_maks[min_indeks] = x

    print(tab_maks)

max10()
        