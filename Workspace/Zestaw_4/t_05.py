def czy_singleton(t, N: int, n : int):
    a = 0
    for i in range(N):
        for j in range(N):
            if t[i][j] == n:
                a += 1

    if a == 1:
        return True
    else:
        return False
    
def sprawdz_tablice(T1, T2, N : int):
    M = N*N
    for i in range(N):
        for j in range(N):
            if czy_singleton(T1, N, T1[i][j]):
                miejsce = M-1
                while T2[miejsce] > T1[i][j]:
                    miejsce -= 1

                for k in range(miejsce):
                    T2[k] = T2[k+1]

                T2[miejsce] = T1[i][j]


n = int(input("Rozmiar: "))
t1 = [[int(input()) for _ in range(n)] for _ in range(n)]
t2 = [0 for _ in range(n*n)]

sprawdz_tablice(t1, t2, n)

print(t1)
print(t2)

