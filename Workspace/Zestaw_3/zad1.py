def przelicz(n : int, system : int):
    tab = [0 for _ in range(10000)]
    znaki = ['0', '1', '2','3', '4', '5', 
             '6', '7', '8' ,'9','A', 'B',
             'C', 'D', 'E', 'F']

    j = 0        
    while n != 0:
        tab[j] = n % system
        n //= system
        j += 1

    print(tab)

    while j > 0:
        j -= 1
        print(znaki[tab[j]], end="")
        

przelicz(int(input("Podaj liczbę: ")), int(input("Podaj system: ")))
print()