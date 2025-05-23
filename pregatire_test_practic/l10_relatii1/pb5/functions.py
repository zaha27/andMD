def citire_matrice(n, m) :
    A = []
    for i in range(n) :
        print(f"rand {i + 1}") 
        lista = []
        for j in range(m) :
            print(f"a[{i}][{j}] = ", end = "")
            x = int(input())
            lista.append(x)
        A.append(lista)
    return A

def afisare_matrice(n, A) : 
    for i in range(n) :
        print(A[i])