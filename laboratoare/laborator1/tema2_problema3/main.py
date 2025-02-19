import functii as f

def main() :
    n = 5
    v = []
    print('citire vector cu {n} elemente \n')
    f.citireLista(v, n)
    
    print('Numarul de elemente negative este:\n')
    print(f.a(v, n))
    

if __name__ == '__main__' :
    main()