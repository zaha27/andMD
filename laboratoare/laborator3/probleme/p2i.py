import laboratoare.laborator3.oplogic as f

def main():
    print("%10s %10s %10s %12s %10s %10s" % ('p', 'q', 'r', 'expr1', 'expr2', 'expr'))
    for p in (False, True):
        for q in (False, True):
            for r in (False, True):
                expr1 = (f.biconditie(q, f.implicatie(r, not(p))))
                expr2 = (f.biconditie(f.implicatie(not(q), p), r))
                expr = expr1 or expr2
                print("%10d %10d %10d %10d %10d %10d" % (p, q, r, expr1, expr2, expr))

if __name__ == '__main__':
    main()
