def odcinki(T):
    for i in range(len(T)):
        for j in range(len(T)):
            if i != j:
                if T[i][0] > T[j][1] or T[i][1] < T[j][0]:
                    if (T[i][1] - T[i][0]) + (T[j][1] - T[j][0]) == 2022:
                        return True
    
    return False