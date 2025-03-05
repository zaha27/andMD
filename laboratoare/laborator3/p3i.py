import oplogic as f

def main():
    print("Tabel de Adevar: \n")
    print("%10s %10s %10s %10s %10s" % ('p', 'q', 'expr1', 'expr2', 'expr'))
    for p in (False, True):
        for q in (False, True):
            expr1 = f.implicatie(p, p and q)      
            expr2 = (p or q) and not(p and q)
            expr = (expr1 and expr2)  == True
            if not(expr) :
                print("%10d %10d %10d %10d %10d" % (p, q, expr1, expr2, expr))
            else: 
                print("***%7d %10d %10d %10d %10d" % (p, q, expr1, expr2, expr))

    
    for p in (False, True):
        for q in (False, True):
            expr1 = f.implicatie(p, p and q)      
            expr2 = (p or q) and not(p and q)
            expr = (expr1 and expr2) == True    
            if expr == 1:
                print("valorile pentru care expresiile sunt egale")
                print("val(p) = %d si val(q) = %d" % (p, q))

if __name__ == '__main__':
    main()

