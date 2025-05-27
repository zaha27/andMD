import functions as f

def main() :
    U = ['Ana', 'Maria', 'Ion', 'George']
    
    M = [
        [0,0,0,1],
        [1,0,1,0],
        [1,1,1,1],
        [1,0,0,0]
    ]
    T = [
        [0,0,1,0],
        [0,0,1,0],
        [1,1,0,1],
        [0,1,0,0]
    ]

    print(f.a(M, T))
    print(f.b(M, T))
    print(f.c(M, T))
    print(f.d(M, T))
    print(f.e(M, T))
    print(f.f(M, T))
    print(f.g(M, T))

    return

if __name__ == "__main__" :
    main()