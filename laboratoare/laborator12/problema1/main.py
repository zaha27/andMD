import functions as f

def main() :
    n = 13
    graf = {
        'a' : ['d'],
        'b' : ['d', 'e'],
        'c' : ['f'],
        'd' : ['i', 'h'],
        'e' : ['h'],
        'f' : ['g'],
        'g' : ['k'],
        'h' : ['k'],
        'i' : ['j'],
        'j' : ['l'],
        'k' : ['l', 'm'],
        'l' : [],
        'm' : []
    }
    #graf = f.citire_graf(n)
    f.afisare_graf(graf)


    print(f.elementele_minimale(graf))
    print(f.elementele_maximale(graf))
    print(f.elementul_maxim(graf))
    print(f.elementul_minim(graf))

    return


if __name__ == '__main__':
    main()