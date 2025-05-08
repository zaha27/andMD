import laboratoare.laborator3.oplogic as f

def main():
    print("Tabel de Adevar: \n")
    print("%10s %10s %10s %10s %10s" % ('p', 'q', 'expr1', 'expr2', 'expr'))
    for p in (False, True):
        for q in (False, True):
            expr1 = f.implicatie(p, q)      
            expr2 = (not(p)) and f.implicatie(not(p or q), p)
            expr = (expr1 and expr2) == True
            if not(expr):
                print("%10d %10d %10d %10d %10d" % (p, q, expr1, expr2, expr))
            else:
                print("***%7d %10d %10d %10d %10d" % (p, q, expr1, expr2, expr))

    print("valorile pentru care expresiile sunt egale")
    for p in (False, True):
        for q in (False, True):
            expr1 = f.implicatie(p, q)      
            expr2 = (not(p)) and f.implicatie(not(p or q), p)
            expr = (expr1 and expr2) == True     
            if expr == 1:
                print("val(p) = %d si val(q) = %d" % (p, q))

if __name__ == '__main__':
    main()
