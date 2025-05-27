import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore
from desenareGraf import desenareGraf
def creareGraf(E, V) :
    G = nx.DiGraph()
    G.add_edges_from(E)
    G.add_nodes_from(V)
    return G

import numpy as np #type: ignore
def inchidere_reflexiva(G, n) :
    A = np.zeros((n,n), dtype = int)
    for i in range(n) :
        for j in range(n) :
            A[i][j] = G[i][j]

    for i in range(n) :
        A[i][i] = 1
    return A
def inchidere_simetrica(G, n) :
    A = np.zeros((n,n), dtype = int)
    for i in range(n) :
        for j in range(n) :
            A[i][j] = G[i][j]
    for i in range(n) :
        for j in range(n) :
            if A[i][j] != A[j][i] :
                A[i][j] = 1
                A[j][i] = 1
    return A

def extrage_lista(G, n) :
    lista = set()
    for i in range(n) :
        for j in range(n) :
            if G[i][j] :
                a = i + 1
                b = j + 1
                tuplu = (a, b)
                lista.add(tuplu)
    return lista


def main() :
    Univers = [1, 2, 3, 4]
    #setul = f.citire_lista_perechi(5)
    setul = {(1,1), (1,2), (1,3), (3,4), (4, 1)}
    f.generare_matrice(setul)
    U = set(Univers)
    
    G = creareGraf(setul, U)
    M_r = nx.adjacency_matrix(G)
    A_r = M_r.todense()
    print(A_r)

    #inchidere reflexiva 
    INCHIDERE = int(input("ce fel de inchidere vrei?\n1-reflexiva\n2-simetrica\n-->"))
    if(INCHIDERE == 1) :
        A_r_inchidere = inchidere_reflexiva(A_r, 4)
    elif INCHIDERE == 2 :
        A_r_inchidere = inchidere_simetrica(A_r, 4)

    x = extrage_lista(A_r_inchidere, 4)
    G = creareGraf(x, U)
    desenareGraf(G)
    plt.show()

if __name__ == "__main__" :
    main()