from functions import citire, max
from functools import reduce
from math import sqrt

def main():
    u = []
    u = citire(7)

#a:
    elemente_pozitive = list(filter(lambda x: x > 0, u))
    elemente_nule = list(filter(lambda x: x == 0, u))
    elemente_negative = list(filter(lambda x: x < 0, u))
    nr_elemente_nule = len(elemente_nule)
    nr_elemente_pozitive = len(elemente_pozitive)
    nr_elemente_negative = len(elemente_negative)

    print(nr_elemente_negative)
    print(nr_elemente_nule)
    print(nr_elemente_pozitive)

#b:
    maximul = reduce(max, elemente_pozitive)
    suma = reduce(lambda x, y: x + y, map(abs, elemente_negative))
    p = list(map(lambda x: x * x, u))
    ps = reduce(lambda x, y: x + y, p)
    norma_euclidiana = sqrt(ps)
    
    print(maximul)
    print(suma)
    print(norma_euclidiana)

if __name__ == "__main__":
    main()
