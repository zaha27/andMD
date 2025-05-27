import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore


def citire_relatie(n) :
    A = set()
    for i in range(n) :
        print(f"{i+1}")
        x = int(input('x = '))
        y = int(input('y = '))
        tuplu = (x, y)
        A.add(tuplu)
    return A

def creareGraf(V, E) :
    G = nx.DiGraph()
    G.add_edges_from(E)
    G.add_nodes_from(V)
    return G

def desenareGraf(G):
    fig, ax = plt.subplots()
    pos = nx.circular_layout(G)
    #node options
    node_options = {
    "node_color": "white",
    "node_size": 500,
    "edgecolors":"black"
    }
    #edge options
    edge_options = {
    "width": 1,
    "edge_color": "black",
    "connectionstyle": 'arc3, rad = 0.10',
    "arrowsize": 12,
    "arrowstyle":"-|>",
    "arrows":True
    }
    node_label_options = {
    "font_size": 10,
    "font_color": "black",
    "verticalalignment": "center",
    "horizontalalignment": "center"
    }
    nx.draw_networkx_nodes(G, pos, ax = ax, **node_options)
    nx.draw_networkx_edges(G, pos, **edge_options)
    nx.draw_networkx_labels(G, pos, **node_label_options)
    ax.set_aspect('equal')
    plt.draw()


def initializare_matrice(n) :
    A = []
    for i in range(n) :
        lista = []  
        for j in range(n) :
            lista.append(0)
        A.append(lista)
    return A

def inchidere_reflexiva(G, n) :
    G_inc_ref = initializare_matrice(n)
    for i in range(n) :    
        for j in range(n) :
            G_inc_ref[i][j] = G[i][j]
            if i == j: G_inc_ref[i][j] = 1
    return G_inc_ref

def inchidere_simetrica(G, n) :
    G_inc_sim = initializare_matrice(n)
    for i in range(n) :
        for j in range(n) :
            G_inc_sim[i][j] = G[i][j]
            if(G_inc_sim[i][j] != G_inc_sim[j][i]) :
                G_inc_sim[i][j] = 1
                G_inc_sim[j][i] = 1
    return G_inc_sim

def extrage_relatii(G, n) :
    A = set()
    for i in range(n) :
        for j in range(n) :
            if G[i][j] == 1 :
                tuplu = (i+1,j+1)
                A.add(tuplu)
    return A
            