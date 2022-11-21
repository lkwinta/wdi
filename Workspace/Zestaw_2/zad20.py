def rozne_cyfry(a : int, b : int):
    for i in range(2, 17):
        znaleziona = True

        k = a
        l = b

        tab = 0

        while k != 0:
            tab |= 1 << k%i 
            k //= i

        while l != 0:
            if tab & (1 << l%i) > 0:
                znaleziona = False
                break
            l //= i
        
        if znaleziona == True:
            return i
    
    return None

print(rozne_cyfry(int(input("A: ")), int(input("B: "))))

