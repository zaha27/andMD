import functii as f
 


def main() :
    univers = ['a', 'b', 'c', 'd']
    dict = f.citire_dictionar(univers) 
    print(dict)
    f.acoperire(dict)
    return

if __name__ == "__main__" :
    main()