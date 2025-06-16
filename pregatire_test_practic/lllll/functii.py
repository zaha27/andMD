import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

def citire_dictionar(univers) :
    u = {}
    print("citire dictionar")
    print("pentru a tasta alti vecini apasati tasta enter")
    for i in univers :
        print(f"pentru nodul {i}")
        u[i] = []
        while True :
            x = input("->")
            if x == "" :
                break
            else : u[i].append(x)
        print()
    return u

def acoperire(d: set) :
    for elem in d :
        print(f"\n{elem} este acoperit de: ", end = "")
        lista_nod = d[elem]
        for nd in lista_nod :
            print(nd, end = " ")