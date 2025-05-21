import numpy as np # type: ignore
import functions as f

def ANB(A, B, n) : 
    C = np.zeros((n,n), dtype = int)
    for i in range(n) :
        for j in range(n) :
            C[i][j] = int(A[i][j] and B[i][j])
    return C

def AVB(A, B, n) : 
    C = np.zeros((n,n), dtype = int)
    for i in range(n) :
        for j in range(n) :
            C[i][j] = int(A[i][j] or B[i][j])
    return C

def A0B(A, B, n):
    C = np.zeros((n, n), dtype=int)
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if A[i][j] and B[j][k]:
                    C[i][k] = 1
                    break
    return C

def ridicare_la_putere(B, n, k) :
    C = B    
    for i in range(k - 1) :
        C = A0B(C, B, n)
    return C


def main() :
    #A = f.citire_matrice(3, "A")
    #B = f.citire_matrice(3, "B")
    A = [[0,1,1],[1,1,0],[0,1,1]]
    B = [[1,0,0],[1,0,1],[0,1,0]]

    C = ANB(A, B, 3)
    f.print_matrix(C)
    print()
    D = AVB(A, B, 3)
    f.print_matrix(D)
    print()
    E = A0B(A, B, 3)
    f.print_matrix(E)
    print()
    F = ridicare_la_putere(B, 3, 3)
    f.print_matrix(F)

if __name__ == "__main__" :
    main()