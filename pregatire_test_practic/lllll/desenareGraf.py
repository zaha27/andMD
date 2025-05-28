import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

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


