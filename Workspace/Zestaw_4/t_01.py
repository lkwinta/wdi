def spirala(N : int):
    t = [[0 for _ in range(N)] for _ in range(N)]
    
    a = 1

    for i in range(N//2):
        for j in range(i, N-i - 1): #w prawo
            t[i][j] = a
            a += 1
        for j in range(i, N-i - 1): # w dół
            t[j][N - i - 1] = a
            a += 1
        for j in range(N - i - 1, i, -1): # w lewo
            t[N - i - 1][j] = a
            a += 1
        for j in range(N - i - 1, i, -1): # w góre
            t[j][i] = a
            a += 1
    
    if N%2 != 0:
        t[N//2][N//2] = a

    return t

print(spirala(3))