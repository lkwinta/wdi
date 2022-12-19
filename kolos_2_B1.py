def rek(N : int, szachownica, w : int = 0, k : int = 0, i : int = 0):
    if w < 0 or k < 0 or w >= N or k >= N or szachownica[w][k] == -1:
        return float("inf")
    else:
        if w == N - 1 and k == N - 1:
            return i

        res = float("inf")
        for i_w in range(w + 1, N):
            res = min( res, rek(N, szachownica, i_w, k, i+1))
        for i_k in range(k + 1, N):
            res = min( res, rek(N, szachownica, w, i_k, i+1))

        return res

def rook(N, L):
    szachownica = [[0 for _ in range(N)] for _ in range(N)]
    for (w, k) in L:
        szachownica[w][k] = -1

    result = rek(N, szachownica)
    
    if result == float("inf"):
        return None
    else:
        return result

print(rook(8, [(7, 7)]))