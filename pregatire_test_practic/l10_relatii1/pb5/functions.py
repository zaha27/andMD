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

def init_matrice(n: int ) -> list :
    A = []
    for i in range(n) :
        lista = []
        for j in range(n) :
            lista.append(0)
        A.append(lista)
    return A

def inversare_matrice(n, A) :
    A_inv = init_matrice(n)
    for i in range(n) :
        for j in range(n) :
            A_inv[i][j] = A[j][i]
    return A_inv

def complement_matrice(n, A) :
    A_compl = init_matrice(n)
    for i in range(n) :
        for j in range(n) :
            if A[i][j] == 0 : 
                A_compl[i][j] = 1
            else : A_compl[i][j] = 0    
    return A_compl

def ridicare_la_patrat(n, A) :
    A_patrat = init_matrice(n)

    for i in range(n) :
        for j in range(n) :
            sum = 0
            for k in range(n) :
                sum = sum or (A[i][k] and A[k][j])
            A_patrat[i][j] = sum
    return A_patrat