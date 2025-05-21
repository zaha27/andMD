import numpy as np  #type: ignore


def inmultire_lista(A, B, i, j, m) :
    rezultat = 0

    lista_unu = A[i]
    lista_doi = []
    for i in range(m) :
        x = B[i][j]
        lista_doi.append(x)
    
    for i in range(len(lista_unu)) :
        x = x or (lista_unu and lista_doi)
        if x == 1 : return 1
    return 0

def AxB(A, B, n, m, p) :
    C = np.zeros((n, p))
    for i in n :
        for j in p :
            C[i][j] = inmultire_lista(A, B, i, j, m)

def main() :
    n = 3
    m = 4
    p = 3
    A = np.zeros((n, m))
    B = np.zeros((m, p))

    
