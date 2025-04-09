import functions as funct
from math import sqrt

def main():
    x = (3.14159, -23.2381, -123.123, 24, -96, 36, 64, -23, -74, -121, 34)

#indirect si cu functii:
    x_pozitive = tuple(filter(funct.pozitiv, x))
    radicali = tuple(map(sqrt, x_pozitive))

#direct si cu lambda:
    radicali_directi = tuple(map(sqrt, filter(lambda x: x > 0, x)))

#print:
    print("metoda indirecta - functii")
    print(radicali)
    print("metoda directa - lambda")
    print(radicali_directi)

if __name__ == "__main__":
    main()
