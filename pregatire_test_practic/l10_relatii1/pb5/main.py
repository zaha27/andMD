import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore


def main() :
    n = int(input("n = "))
    A = f.citire_matrice(n, n)
    f.afisare_matrice(n, A)
    A_inv = f.inversare_matrice(n, A)
    f.afisare_matrice(n, A_inv)
    A_compl = f.complement_matrice(n, A)
    f.afisare_matrice(n, A_compl)
    A_patrat = f.ridicare_la_patrat(n, A)
    f.afisare_matrice(n, A_patrat)

    lista = f.lista_perechi(n, A)
    print(lista)

    V = list(range(1, n+1))
    E = lista

    G = f.creareGraf(V, E)
    f.desenareGraf(G)
    print(V)

    plt.show()
    

if __name__ == "__main__" :
    main()