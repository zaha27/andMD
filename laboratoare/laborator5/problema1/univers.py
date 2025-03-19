def citireUnivers():
    Univers = []
    n = int(input("n = "))
    for i in range(0, n):
        print("Univers[",i,"]=", end='')
        Univers.append(int(input()))
    return Univers