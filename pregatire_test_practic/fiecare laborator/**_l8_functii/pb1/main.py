from functii import functia1, functia2


def main() :
    x = list(range(-10,11))
    y = list(range(-10,11))
    z = list(range(-10,11))
    
    rez_f1 = list(map(functia1, x))
    
    rez_f2 = list(map(functia2, x, y, z))
    
    for i in range(len(x)) :
        print(f"f1[{i}] = {rez_f1[i]}")
    for i in range(len(x)) :
        print(f"f2[{i}] = {rez_f2[i]}")

if __name__ == '__main__' :
    main()