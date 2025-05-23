def implicatie(p, q) :
    if p == 1 and q == 0 :
        return False
    else : return True
def sau_exclusiv(p, q) :
    p = int(p)
    q = int(q)
    return bool((p + q) % 2)

def biconditie(p, q) :
    return implicatie(p, q) and implicatie(q, p)

def unu(a, b, c, d, e) :
    return implicatie(a, b)

def doi(a, b, c, d, e) :
    return a or b

def trei(a, b, c, d, e) :
    return sau_exclusiv(b, c)

def patru(a, b, c, d, e) :
    return biconditie(d, c)

def cinci(a, b, c, d, e) :
    return implicatie(e, a and d)

def print_tabel(a, b, c, d, e, decl1, decl2, decl3, decl4, decl5) :
    if(decl1 and decl2 and decl3 and decl4 and decl5) :
        print(f"*-->{a:<5}{b:<5}{c:<5}{d:<5}{e:<5}{decl1:<5}{decl2:<5}{decl3:<5}{decl4:<5}{decl5:<5}")
    print(f"{' ':<4}{a:<5}{b:<5}{c:<5}{d:<5}{e:<5}{decl1:<5}{decl2:<5}{decl3:<5}{decl4:<5}{decl5:<5}")

