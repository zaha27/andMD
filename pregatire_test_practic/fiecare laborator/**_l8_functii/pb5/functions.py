def citire_lista_cuvinte (n) :
    n = 0
    lista = []
    while True :
        try :
            n = n + 1
            v = input(f"cuvantul {n}: ")
            lista.append(v)
        except EOFError :
            print(f"gata lista")
            break

    return lista
    
def majuscule(lista) :
    f = lambda word : str.upper(word)
    lista = list(map(f, lista))
    return lista

from functools import reduce
def concatenare(lista) :
    f = lambda x, y : x + y
    lista = reduce(f, lista)
    return lista
    