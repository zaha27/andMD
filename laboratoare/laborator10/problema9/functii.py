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
