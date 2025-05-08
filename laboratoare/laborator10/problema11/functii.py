def citire_relatii(n, m):
    a = []
    for i in range(m) :
        linie = []
        for j in range(m) :
            x = 0
            linie.append(x)
            
    for i in range(n):
        first = input("(")
        print(",", end = " ")
        last = input(")")
        a[first - 1][last - 1] = 1
    return a

def citire_matrice(n):
    a = []
    for i in range(n):
        linie = []
        for j in range(n):
            x = int(input(f"a[{i}][{j}] = "))
            linie.append(x)
        a.append(linie)
    return a

def afisare_matrice(a, n):
    for i in range(n):
        print(a[i])
