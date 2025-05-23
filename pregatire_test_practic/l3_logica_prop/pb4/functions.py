def implicatie(p, q) :
    if p == 1 and q == 0 :
        return False
    else : return True

def declaratie_bogdan(florin, bogdan, stan) :
    if stan == 1 and florin == 0 :
        return True
    else : return False

def declaratie_stan(florin, bogdan, stan) :
    return implicatie(bogdan, florin)

def declaratie_florin(florin, bogdan, stan) :
    if florin == 0 and (bogdan or stan) :
        return True
    else : return False

def print_tabel(p, q, r, decl1, decl2, decl3) :
    if(decl1 and decl2 and decl3) :
        print(f"*** {p:<5}{q:<5}{r:<5}{decl1:<10}{decl2:<10}{decl3:<10}")
    print(f"{' ':<4}{p:<5}{q:<5}{r:<5}{decl1:<10}{decl2:<10}{decl3:<10}")

