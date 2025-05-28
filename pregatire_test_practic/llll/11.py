import functions as f
import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore
from pregatire_test_practic.lllll.desenareGraf import desenareGraf
import functii_hase as fh

def main() :
    lista_noduri = ['a', 'b', 'c']
    d = fh.citire_hasse(lista_noduri)
    print(d)

    
    return


if __name__ == "__main__" :
    main()