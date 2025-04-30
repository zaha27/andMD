import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import functii_graf as fg
import functii_relatii as fr
import numpy as np # type: ignore

def reprezentareMatriceala(relatie, n):
    M = np.zeros((n,n))
    M = M.astype(int)

    for elem in relatie:
        a = elem[0]
        b = elem[1]
        M[a-1][b-1] = 1
    return M

def main():
    A = [1,2,3,4,5,6]
    R = fr.relatie(A)
    M = reprezentareMatriceala(R, len(A))
    print(M)

    n = int(input("Numarul de noduri din graf: "))
    V = fg.citesteListaNodurilor(n)
    E = fg.citesteLaturile(V)
    G = fg.creareGraf(V, E)
    fg.desenareGraf(G)
    M_R = nx.adjacency_matrix(G)
    A_R = M_R.todense()

    print()
    print("Lista nodurilor: ", V)
    print("Lista laturilor: ", E)
    
    print("Matricea de adiacenta: ")
    print(A_R)

    plt.show()

if __name__ == '__main__':
    main()
