import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore


def citire_matrice(n, m) :
    A = []
    for i in range(n) :
        print(f"rand {i + 1}") 
        lista = []
        for j in range(m) :
            print(f"a[{i}][{j}] = ", end = "")
            x = int(input())
            lista.append(x)
        A.append(lista)
    return A

def afisare_matrice(n, A) : 
    for i in range(n) :
        print(A[i])

def init_matrice(n: int ) -> list :
    A = []
    for i in range(n) :
        lista = []
        for j in range(n) :
            lista.append(0)
        A.append(lista)
    return A

def inversare_matrice(n, A) :
    A_inv = init_matrice(n)
    for i in range(n) :
        for j in range(n) :
            A_inv[i][j] = A[j][i]
    return A_inv

def complement_matrice(n, A) :
    A_compl = init_matrice(n)
    for i in range(n) :
        for j in range(n) :
            if A[i][j] == 0 : 
                A_compl[i][j] = 1
            else : A_compl[i][j] = 0    
    return A_compl

def ridicare_la_patrat(n, A) :
    A_patrat = init_matrice(n)

    for i in range(n) :
        for j in range(n) :
            sum = 0
            for k in range(n) :
                sum = sum or (A[i][k] and A[k][j])
            A_patrat[i][j] = sum
    return A_patrat

def lista_perechi(n : int, A : list) -> list :
    m = n * n
    lista = []
    for i in range(n) :
        for j in range(n) :
            if A[i][j] == 1 :
                lista.append((i+1, j+1))
    return lista

def creareGraf(V :list, E:list) :
    G = nx.DiGraph()
    G.add_nodes_from(V)
    G.add_edges_from(E)
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