import numpy as np # type: ignore
import networkx as nx# type: ignore
import matplotlib.pyplot as plt # type: ignore

def deseneaza_graf(noduri, muchii):
    G = nx.DiGraph()               # Graf orientat
    G.add_nodes_from(noduri)
    G.add_edges_from(muchii)

    pos = nx.circular_layout(G)    # Layout circular

    node_opts = {
        "node_color": "white",
        "node_size": 500,
        "edgecolors": "black"
    }

    edge_opts = {
        "width": 1,
        "edge_color": "black",
        "connectionstyle": 'arc3, rad=0.10',
        "arrowsize": 12,
        "arrowstyle": "-|>",
        "arrows": True
    }

    label_opts = {
        "font_size": 10,
        "font_color": "black",
        "verticalalignment": "center",
        "horizontalalignment": "center"
    }

    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax, **node_opts)
    nx.draw_networkx_edges(G, pos, ax=ax, **edge_opts)
    nx.draw_networkx_labels(G, pos, ax=ax, **label_opts)

    ax.set_aspect("equal")
    plt.title("Graful relației a | b")
    plt.show()


def relatie(a, b, rez) :
    if a == 0 : return
    if b % a == 0 :
        rez.append((a,b))

def reprezentare_matriceala(rez, n) :
    matrix = np.zeros((n, n), dtype = int)
    for tuplu in rez :
        i = tuplu[0]
        j = tuplu[1]
        matrix[i - 1][j - 1] = 1
    return matrix

def main() :
    A = set(range(1, 7, 1))
    n = len(A)
    rez = []
    for a in A :
        for b in A :
            relatie(a, b, rez)
    print(rez)
    matrix = np.zeros((n,n), dtype = int)
    matrix = reprezentare_matriceala(rez, n)
    print(matrix)

    noduri = list(A)
    muchii = rez
    deseneaza_graf(noduri, muchii)
    return

if __name__ == "__main__" :
    main()