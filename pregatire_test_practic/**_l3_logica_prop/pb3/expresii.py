import oplogic as op

def i_unu(p, q) :
    unu = p and q
    doi = op.implicatie(p, unu)
    return doi

def i_doi(p, q) :
    unu = p or q
    doi = not(p and q)
    return unu and doi