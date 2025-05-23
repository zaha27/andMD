def citire_vector(n) :
    lista = []
    for i in range(n) :
        x = int(input(f"v[{i}]"))
        lista.append(x)
    return lista

def numere_pozitive(lista, n) :
    pozitive_lambda = lambda x : x > 0
    rez = []
    rez = list(filter(pozitive_lambda, lista))
    return rez

def numere_negative(lista, n ) :
    pozitive_lambda = lambda x : x < 0
    rez = []
    rez = list(filter(pozitive_lambda, lista))
    return rez

def numere_nule(lista, n) :
    pozitive_lambda = lambda x : x == 0
    rez = []
    rez = list(filter(pozitive_lambda, lista))
    return rez

from functools import reduce
def max_pozitive(lista) :
    f = lambda x, y: x if x > y else y 
    max = reduce(f, lista)
    return max

def sum_negative(lista) :
    f = lambda x : abs(x)
    lista = map(f, lista) 
    g = lambda x, y : x + y
    sum = reduce(g, lista)
    return sum

def norma_euclidiana(lista) :
    f = lambda x : abs(x)
    g = lambda x, y : x + y
    h = lambda x : x * x
    lista = map(f, lista)
    lista = map(h, lista)
    norma = int(reduce(g, lista))
    return norma