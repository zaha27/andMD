def i(p, q) :
    unu = not(p) or q
    doi = p and not(q)
    return unu or doi

def ii(p, q) :
    unu = not(p) or q
    doi = p and not(q)
    return not(unu and doi)

def iii(p, q, r) :
    unu = p and (q or r)
    doi = (p and q) or (p and r)
    return biconditie(unu, doi)

def iv(p, q, r) :
    unu = p and q
    doi = not p or r
    trei = q or r
    patru = unu and doi
    return implicatie(patru, trei)

def v(p, q) :
    unu = implicatie(p, q)
    doi = p and unu
    trei = q
    return implicatie(doi, trei)

#operatii -->
def implicatie(p, q) :
    if p == 1 and q == 0 :
        return False
    else : return True

def biconditie(p, q) :
    return implicatie(p, q) and implicatie(q, p)


#test tautologie -->
def tautologie(f_arg, cati_parametri) :
    u = [False, True]
    if cati_parametri == 2 :
        for p in u :
            for q in u :
                if f_arg(p, q) == False :
                    return False
        return True
    elif cati_parametri == 3 :
        for p in u :
            for q in u :
                for r in u :
                    if f_arg(p, q, r) == False :
                        return False
        return True       