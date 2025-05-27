def implicatie(p, q):
    return (not p) or q
    
def sau_exclusiv(p, q) :
    return (not(p) and q) or (not(q) and p)

def biconditie(p, q) :
    return implicatie(p, q) and implicatie(q, p)