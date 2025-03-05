def implicatie(p, q):
    if p:
        return q
    else:
        return True

def implica(p, q):
    return not p or q

def biconditie(p, q):
    implicatie1 = implicatie(p, q);
    implicatie2 = implicatie(q, p);
    rezultat = implicatie1 and implicatie2;
    return rezultat

def sau_exclusiv(p, q):
    rezultat = (p and not(q)) or (not(p) and q)
    return rezultat
