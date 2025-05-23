def implicatie(p, q) :
    if p == 1 and q == 0 : return False
    return True

def biconditie(p, q) :
    return implicatie(p, q) and implicatie(q, p)

def i(p, q, r) :
    unu = p or q
    doi = not p or r
    trei = q or r
    x = unu and doi 
    return implicatie(x, trei)

def ii(p, q, r) :
    unu = implicatie(p, q)
    doi = implicatie(q, r) 
    trei = implicatie(p, r)
    x = unu and doi
    return implicatie(x, trei)

def iii(a, b) :
    unu = biconditie(b, implicatie(b, a))
    doi = a
    return implicatie(unu, doi)