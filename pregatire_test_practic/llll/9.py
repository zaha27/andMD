import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore
from pregatire_test_practic.lllll.desenareGraf import desenareGraf
def creareGraf(E, V) :
    G = nx.DiGraph()
    G.add_edges_from(E)
    G.add_nodes_from(V)
    return G

def main() :
    Univers = [1, 2, 3, 4]
    #setul = f.citire_lista_perechi(5)
    setul = {(1,1), (1,2), (1,3), (3,4), (4, 1)}
    f.generare_matrice(setul)
    U = set(Univers)
    
    G = creareGraf(setul, U)
    desenareGraf(G)
    plt.show() 
    M_r = nx.adjacency_matrix(G)
    A_r = M_r.todense()
    print(A_r)

#de verificat daca e de echivalenta, de ordine

    return

if __name__ == "__main__" :
    main()