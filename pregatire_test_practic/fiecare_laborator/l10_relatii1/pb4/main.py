import numpy as np  #type: ignore


def inmultire_lista(A, B, i, j, m):
    for k in range(m):
        if A[i][k] and B[k][j]:
            return 1
    return 0

def AxB(A, B, n, m, p) :
    C = np.zeros((n, p), dtype = int)
    for i in range(n) :
        for j in range(p) :
            C[i][j] = inmultire_lista(A, B, i, j, m)
    return C

def main() :
    n = 3
    m = 4
    p = 3
    A = [
        [0, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 0]
    ]

    B = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]

    C = AxB(A, B, n, m, p)
    print(C)

if __name__ == "__main__" :
    main()
