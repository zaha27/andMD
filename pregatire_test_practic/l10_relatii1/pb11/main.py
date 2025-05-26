import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

def main() :
    n = input('n = ')
    A = {1,2,3,4}
    R_a = set()
    R_a = f.citire_relatie(n)
    print(R_a)

    V = A
    E = R_a
    G = f.creareGraf(V, E)

    print(f"Inchiderea Reflexiva")
    f.desenareGraf(G)
    plt.show()
    return


if __name__ == "__main__" :
    main()