def citire_lista(n) :
    lista = []
    for i in range(n) :
        print(f"a[{i}] = ", end='')
        x = input()
        lista.append(x)
    return lista

def citire_matrice(n, nume) :
    matrice = []
    for k in range(n) :
        lista = []
        for i in range(n) :
            print(f"{nume}[{k}][{i}] = ", end='')
            x = input()
            lista.append(x)
        matrice.append(lista)
    return matrice

def print_matrix(A) :
    for lista in A :
        print(lista)
