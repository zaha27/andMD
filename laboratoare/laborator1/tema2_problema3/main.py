import functii as f

def main() :
    n = 5
    v = [-1,2,-3,4,5]
    #print('citire vector cu {n} elemente \n')
    #f.citireLista(v, n)
    
    print('Numarul de elemente negative este:')
    print(f.a(v, n))

    print('Produsul elementelor este:')
    print(f.b(v, n))

if __name__ == '__main__' :
    main()