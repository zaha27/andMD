import oplogic as f

def expresie1(p, q):
    return ((not(p) or q) and (p and not(q)))

def expresie2(p, q):
    return not((p and not(q)) and (not(p) or q))

def expresie3(p, q, r):
    first = p and (q or r)
    second = p and q or p and r 
    return f.biconditie(first, second)

def expresie4(p, q, r):
    first = p or q
    second = not(p) or r
    third = q or r
    fourth = first and second
    return f.implica(fourth, third)

def expresie5(p, q):
    first = p and f.implica(p, q)
    return f.implica(first, q)

def e_tautologie_two(expresie):
    for p in [True, False]:
        for q in [True, False]:
            if not expresie(p, q):
                return False
    return True

def e_tautologie_three(expresie):
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                if not expresie(p, q, r):
                    return False
    return True
     


            