def krole():
    szachownica = [[0 for _ in range(201)] for _ in range(201)]
    lista_kroli = [(int(input(f"w{i}: ")), int(input(f"k{i}: "))) for i in range(100)]

    for (w, k) in lista_kroli:
        d_pion = abs(100 - w)
        d_poziom = abs(100 - k)

krole()