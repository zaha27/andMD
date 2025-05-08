import laboratoare.laborator3.oplogic as f

def main():
    print("%10s %10s %10s %10s %10s %10s %10s" % ('p', 'q', 'r', 'expr1', 'expr2', 'expr3', 'expr'))
    for p in (False, True):
        for q in (False, True):
            for r in (False, True):
                expr1 = p or q
                expr2 = not(p) or r
                expr3 = q or r 
                expr = f.implicatie(expr1 and expr2, expr3)
                print("%10d %10d %10d %10d %10d %10d %10d" % (p, q, r, expr1, expr2, expr3, expr))

if __name__ == '__main__':
    main()
