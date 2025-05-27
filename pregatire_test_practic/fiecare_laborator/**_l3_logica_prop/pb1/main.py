import oplogic as op

def main() :
    p = False
    q = False
    print(f"{'p':<10} {'q':<10} {'implicatie':<12} {'biconditie':<12} {'sau exclusiv':<12}")
    for p in [False, True] :
        for q in [False, True] :
            op1 = op.implicatie(p, q)
            op2 = op.biconditie(p, q)
            op3 = op.sau_exclusiv(p, q)
            print(f"{p:<10} {q:<10} {op1:<12} {op2:<12} {op3:<12}")
    return

if __name__ == "__main__" :
    main()