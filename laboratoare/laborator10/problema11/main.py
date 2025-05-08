from functii import citire_relatii, afisare_matrice
import proprietati as p

def main():
    n = 6
    m = 4

    matrice = citire_relatii(n, m)
    afisare_matrice(matrice, n)



if __name__ == '__main__':
    main()
