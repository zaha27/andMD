def citireLista(n) :
    v = []
    for i in range(n) :
        x = int(input())
        v.append(x)
    return v

def citireMatrice(n) :
    A = [[]]
    for i in range(n) :
        A[i] = citireLista(n)
    return A