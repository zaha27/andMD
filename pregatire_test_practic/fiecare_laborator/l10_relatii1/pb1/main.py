import functions as f

def main() :
    A = set(range(5))
    B = set(range(4))
    reza = []
    rezb = []
    rezc = []
    rezd = []
    reze = []
    rezf = []
    for a in A :
        for b in B :
            f.a(a, b, reza)
            f.b(a, b, rezb)
            f.c(a, b, rezc)
            f.d(a, b, rezd)
            f.e(a, b, reze)
            f.f(a, b, rezf)
    print(reza)
    print(rezb)
    print(rezc)
    print(rezd)
    print(reze)
    print(rezf)


if __name__ == "__main__" :
    main()