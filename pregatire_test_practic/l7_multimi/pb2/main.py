import functions as f

def main() :
    A = {'a', 'b', 'c'} 
    B = {'a', 'b', 'd', 'e'}

    print(f"{'x':<10} {'A':<10} {'B':<10} {'AuB':<10} {'A∩B':<10} {'A-B':<10} {'B-A':<10} {'A^B':<10}")

    U = set(A | B)
    for x in U : 
        print(f"{x:<10} {x in A:<10} {x in B:<10} {x in A | B:<10} {x in A & B:<10} {x in A - B:<10} {x in B - A:<10} {x in A ^ B:<10}")
    return

if __name__ == '__main__' :
    main()