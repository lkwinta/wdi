import random

def roznica_dlugosci(t, n : int) -> int:
    maks_ujemna = 2
    maks_dodatnia = 2

    obecna_ujemna = 2
    obecna_dodatnia = 2

    dodatnie_r = 0
    ujemne_r = 0

    for i in range(1, n):
        r = t[i] - t[i - 1]
        if r > 0: 
            if r == dodatnie_r:
                obecna_dodatnia += 1
            else:
                if obecna_dodatnia > maks_dodatnia:
                    maks_dodatnia = obecna_dodatnia 

                obecna_dodatnia = 2
                dodatnie_r = t[i] - t[i - 1]
        elif r < 0: 
            if r == ujemne_r:
                obecna_ujemna += 1
            else:
                if obecna_ujemna < maks_ujemna:
                    maks_ujemna = obecna_ujemna
                
                obecna_ujemna = 2
                ujemne_r = t[i] - t[i - 1]
    
    if obecna_dodatnia > maks_dodatnia:
        maks_dodatnia = obecna_dodatnia
    if obecna_ujemna > maks_ujemna:
        maks_ujemna = obecna_ujemna
         
    return maks_dodatnia - maks_ujemna

n = int(input("Ilosc elementow: "))
t = [random.randint(1,99) for _ in range(n)]

print(roznica_dlugosci(t, n))