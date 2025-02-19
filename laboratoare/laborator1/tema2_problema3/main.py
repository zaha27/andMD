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

    print('Suma elementelor este:')
    print(f.c(v, n))

    print('Produsul elementelor negative este:')
    print(f.d(v, n))

    print('Maximul elementelor este:')
    print(f.e(v, n))

    print('Minimul elementelor este:')
    print(f.f(v, n))
    

if __name__ == '__main__' :
    main()
