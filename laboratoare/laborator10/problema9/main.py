from functii import citire_matrice, afisare_matrice
import proprietati as p

def main():
    n = 4
    matrice = citire_matrice(n)
    afisare_matrice(matrice, n)

    print("\nProprietatea reflexivitate:", end=" ")
    print(p.reflexivitatea(matrice, n))

    print("Proprietatea antireflexivitate:", end=" ")
    print(p.antireflexivitatea(matrice, n))

    print("Proprietatea simetrie:", end=" ")
    print(p.simetria(matrice, n))

    print("Proprietatea asimetrie:", end=" ")
    print(p.asimetria(matrice, n))

    print("Proprietatea antisimetrie:", end=" ")
    print(p.antisimetria(matrice, n))

    print("Proprietatea tranzitivitate:", end=" ")
    print(p.tranzitiva(matrice, n))

if __name__ == '__main__':
    main()
