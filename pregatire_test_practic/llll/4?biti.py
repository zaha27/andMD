import functions as f

def main() :
    print(f"tabel de apartenenta")
    print()
    C = set()
    A = {'a','b','c'}
    B = {'a','b','c','e'}
    C = A | B
    D = A.symmetric_difference(B)
    print(f"{'A':<3}{'B':<3}{'AUB':<5}{'A∩B':<5}{'A-B':<5}{'B-A':<5}{'A^B':<5}")
    for x in C :
        print(f"{x in A:<3}{x in B:<3}{x in C:<5}{x in A & B:<5}{x in A - B:<5}{x in B - A:<5}{x in D:<5}")    
    return

#

if __name__ == "__main__" :
    main()