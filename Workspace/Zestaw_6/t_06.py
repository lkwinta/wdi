def podciagi(T, p : int, k : int):
    if p != k and k != len(T):
        print(T[p:k+1])
        podciagi(T, p + 1, k)
        podciagi(T, p, k + 1)

T = [1,2,3,4]
podciagi(T, 0, 1)
