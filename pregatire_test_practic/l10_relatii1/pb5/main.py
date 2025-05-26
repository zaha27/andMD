import functions as f

def main() :
    n = int(input("n = "))
    A = f.citire_matrice(n, n)
    f.afisare_matrice(n, A)
    A_inv = f.inversare_matrice(n, A)
    f.afisare_matrice(n, A_inv)
    A_compl = f.complement_matrice(n, A)
    f.afisare_matrice(n, A_compl)
    A_patrat = f.ridicare_la_patrat(n, A)
    f.afisare_matrice(n, A_patrat)

    

if __name__ == "__main__" :
    main()