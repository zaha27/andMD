import matplotlib.pyplot as plt # type: ignore
import networkx as nx # type: ignore

def desenareGraf(G):
    fig, ax = plt.subplots()
    pos = nx.circular_layout(G)

    # node options
    node_options = {
        "node_color": "white",
        "node_size": 500,
        "edgecolors": "black"
    }

    # edge options
    edge_options = {
        "width": 1,
        "edge_color": "black",
        "connectionstyle": 'arc3, rad = 0.10',
        "arrowsize": 12,
        "arrowstyle": "-|>",
        "arrows": True
    }

    node_label_options = {
        "font_size": 10,
        "font_color": "black",
        "verticalalignment": "center",
        "horizontalalignment": "center"
    }

    nx.draw_networkx_nodes(G, pos, ax=ax, **node_options)
    nx.draw_networkx_edges(G, pos, **edge_options)
    nx.draw_networkx_labels(G, pos, **node_label_options)

    ax.set_aspect('equal')
    plt.draw()

def citesteListaNodurilor(n:int) -> list:
    V = []
    print("Introduceti Nodurile")
    for i in range(n) :
        print('Nodul ', i+1, end = ' ')
        v = input()
        V.append(v)
    return V

def citesteLaturile(V:list) -> list: 
    E = []
    print('Laturile grafului sunt(trebuie date sub forma a-b):')
    try: 
        while True :
            e = input("> ")
            a,b = e.split('-')
            if ((a in V) and (b in V)):
                E.append((a, b))
            else :
                print('Nu ati introdus nodurile corect')
    except EOFError :
        pass
    return E

def creareGraf(V:list, E:list):
    G = nx.DiGraph()
    G.add_nodes_from(V)
    G.add_edges_from(E)
    return G
