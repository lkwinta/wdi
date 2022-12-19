def czy_szachuja(wieze, N):
    kolumny = [False]*N
    wiersze = [False]*N
    
    for [w, k] in wieze:
        kolumny[k] = True
        wiersze[w] = True
    
    for i in range(N):
        if not kolumny[i] or not wiersze[i]:
            return False
    
    return True

def move(T):
    N = len(T)
    lista_wiezy = []
    #wiersz
    for w in range(len(T)):
        #kolumna
        for k in range(len(T)):
            if T[w][k]:
                lista_wiezy.append([w, k])
    
    czy_szachuja(lista_wiezy, len(T))
    for i in range(len(lista_wiezy)):
        stara = lista_wiezy[i]
        for w in range(N):
            lista_wiezy[i][0] = w
            if czy_szachuja(lista_wiezy, N):
                return ((stara[0], stara[1]),)
