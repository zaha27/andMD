import functions as f 

def main() :
    lista = [-2, -3, -4, 0, 0, 0, 2, 3, 5, 7]
    n = len(lista)
    #lista = f.citire_vector(n) 
    pozitive = f.numere_pozitive(lista, n)
    print(f"lista cu numere pozitive {pozitive} si numarul lor: {len(pozitive)}")

    negative = f.numere_negative(lista, n)
    print(f"lista cu numere negative {negative} si numarul lor: {len(negative)}")

    nule = f.numere_nule(lista, n)
    print(f"lista cu numere nule {nule} si numarul lor: {len(nule)}")

    print(f"maximul : {f.max_pozitive(pozitive)}")
    print(f"suma nr negative : {f.sum_negative(negative)}")
    print(f"norma euclidiana : {f.norma_euclidiana(lista)}")
    return


if __name__ == "__main__" :
    main() 