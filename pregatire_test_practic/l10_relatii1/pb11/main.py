import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

def main() :
    n = int(input('n = '))
    A = {1,2,3,4}
    R_a = set()
    R_a = f.citire_relatie(n)
    print(R_a)

    V = A
    E = R_a
    G = f.creareGraf(V, E)
    M_R = nx.adjacency_matrix(G)
    A_R = M_R.todense()


    print(f"Inchiderea Simetrica") 
    G_inc_sim_py = f.inchidere_simetrica(A_R, 4)
    E_sim = f.extrage_relatii(G_inc_sim_py, 4)
    G_inc_sim = f.creareGraf(V, E_sim)
    f.desenareGraf(G_inc_sim)
    plt.show()
    return


if __name__ == "__main__" :
    main()