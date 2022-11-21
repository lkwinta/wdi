def sequence(T):
    znalezione = [[0,0] for _ in range(len(T)//2)]
    licznik_znalezione = 0

    dlugosc_obecna = 1
    indeks_start = 0

    for i in range(1, len(T)):
        if T[i - 1] < T[i]:
            dlugosc_obecna += 1
        else:
            if dlugosc_obecna >= 2:
                znalezione[licznik_znalezione] = [indeks_start, i - 1]
                licznik_znalezione += 1
            #end if
            
            indeks_start = i
            dlugosc_obecna = 1
        #end if
    
    if dlugosc_obecna >= 2:
        znalezione[licznik_znalezione] = [indeks_start, len(T)-1]
        licznik_znalezione += 1
    #end if

    if licznik_znalezione < 2:
        return False
    #end if

    for i in range(licznik_znalezione):
        for j in range(licznik_znalezione):
            if i != j:
                if T[znalezione[i][0]] > T[znalezione[j][1]] or T[znalezione[j][0]] > T[znalezione[i][1]]:
                    return True
                #end if
            #end if
        #end for
    #end for
    
    return False

T1 = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]
T2 = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]
                
print(sequence(T1))
print(sequence(T2))