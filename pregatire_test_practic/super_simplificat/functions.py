def pb1_recursivitate(a : int, b : int) -> int :
    if b == 0 :
        return a
    return pb1_recursivitate(b, a%b)

def implicatie(p, q) :
    if p == 1 and q == 0 :
        return 0
    else : return 1
def pb2_tabel() :
    u = [False, True]
    print(f"{' ':<2}{'a':<3}{'b':<3}{'a->b':5}")
    for a in u :
        for b in u :
            if implicatie(a, b) == 1 :
                print(f"**{a:<3}{b:<3}{implicatie(a,b):<5}")
            else :
                print(f"{' ':<2}{a:<3}{b:<3}{implicatie(a,b):<5}")
    
