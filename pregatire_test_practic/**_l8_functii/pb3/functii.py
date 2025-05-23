def citire_vector(n, nr, nume) :
    u = [] 
    print(f"vector {nr}")
    for i in range(n) :
        print(f"{str(nume)}[{i}] = ")
        x = input()
        u.append(x)
    return u
