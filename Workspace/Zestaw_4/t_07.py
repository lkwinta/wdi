def polacz_tab(T1, T2, N):
    M = N*N
    for i in range(N):
        miejsce = M-1
        for j in range(N-1, -1, -1):
            while T2[miejsce] >= T1[i][j]:
                miejsce -= 1
            for k in range(miejsce):
                T2[k] = T2[k+1]
            
            T2[miejsce] = T1[i][j]

n = int(input("Rozmiar: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]
t2 = [0 for _ in range(n*n)]

polacz_tab(t1, t2, n)

print(t1)
print(t2)