def osiem_hetmanow(szachownica, N : int = 8, licznik : int = 0):
    if licznik == 8:
        return True
    for w in range(N):
        for k in range(N):
            if szachownica[w][k] == 0:
                #zaszachuj wiersz
                for i in range(N):
                    szachownica[w][i] += 1
                #zaszachuj kolumne
                for i in range(N):
                    szachownica[i][k] += 1

                 

                #odszachuj wiersz
                for i in range(N):
                    szachownica[w][i] -= 1
                #odszachuj kolumne
                for i in range(N):
                    szachownica[i][k] -= 1

def wywolanie():
    szachownica = [[0 for _ in range(8)] for _ in range(8)]
    return osiem_hetmanow(szachownica)