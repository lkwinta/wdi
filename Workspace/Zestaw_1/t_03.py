#da się zrobić bez tablic
#liczyć dwa ciągi jednocześnie (ten do dodawania i odejmowania)


def suma_podciagu(zadana_suma : int):
    if zadana_suma == 1:
        return True

    pierwszy_1 = 0
    drugi_1 = 1
    obecny_1 = 1

    pierwszy_2 = 0
    drugi_2 = 0
    obecny_2 = 1

    suma = 1

    while obecny_1 <= zadana_suma:
        if suma < zadana_suma:
            suma += obecny_1
            
            pierwszy_1 = drugi_1
            drugi_1 = obecny_1
            obecny_1 = pierwszy_1 + drugi_1
    
        if suma > zadana_suma:
            suma -= obecny_2

            pierwszy_2 = drugi_2
            drugi_2 = obecny_2
            obecny_2 = pierwszy_2 + drugi_2
    
        if suma == zadana_suma:
            #print("Tak")
            #zakazana składnia ale nie jest częścią rozwiązania :p
            #print(wyrazy[poczatek : koniec]) 
            return True

    return False

#zadana_suma = int(input("Podaj sume: "))
#print(suma_podciagu(zadana_suma))

for i in range(10, 10000):
   print(f"{i} {suma_podciagu(i)}")