import numpy as np # type: ignore

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

def predicat1(x, y) :
    r = x*x == y
    return r
def predicat2(x, y) :
    r = x*y == 1
    return r
def pb3_cuantificatori() :
    U1 = range(-10, 11)
    U2 = range(-100, 101)
    U3 = np.arange(-10, 10.1, 0.1)

    #a
    stare_a = True
    for x in U1 :
        ok = 0
        for y in U2 :
            if(predicat1(x, y) == 1) :
                ok = 1
        if ok == 0 : 
            stare_a = False
    print(f"Stare a):{stare_a}")
    
    #b
    stare_b = True
    for y in U2 :
        ok = 0
        for x in U1 :
            if(predicat1(x, y) == 1) :
                ok = 1
        if ok == 0 : 
            stare_b = False
    print(f"Stare b):{stare_b}")

    stare_c= False
    for x in U3 :
        ok = 1
        for y in U3 :
            if(predicat2(x, y) == 0) :
                ok = 0
        if ok == 1 : 
            stare_c = True
    print(f"Stare c):{stare_c}")    

    lista_d = []
    stare_d = True
    for x in U3 :
        ok = 0
        for y in U3 :
            if(predicat2(x, y) == 1) :
                ok = 1
        if ok == 0 : 
            stare_a = False
    print(f"Stare d):{stare_d}")

def pb2_argumentatie() :
    
    u = [False, True]
    ok = 1
    for a in u :
        for b in u :
            for c in u :
                ip1 = implicatie(a, b and c)
                ip2 = not b
                expr = implicatie(ip1 and ip2, not a)
                if not expr :
                    ok = 0
    print(bool(ok))