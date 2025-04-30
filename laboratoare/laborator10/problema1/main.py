import functii as f

def main():
    A = f.citireLista(5)
    B = f.citireLista(4)

    ordonate = f.relatie(A, B)

    print("perechi:")
    for pereche in ordonate:
        print(pereche)

if __name__ == '__main__':
    main()
