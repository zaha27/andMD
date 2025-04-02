def reuniune(A, B):
    C = set()
    for x in A:
        C.add(x)
    for y in B:
        C.add(y)
    return C

def intersectie(A, B):
    C = set()
    for x in A:
        if x in B:
            C.add(x)
    return C

def diferenta(A, B):  # A - B
    C = set()
    for x in A:
        if x not in B:
            C.add(x)
    return C

def diferenta_simetrica(A, B):
    C = set()
    for x in A:
        if x not in B:
            C.add(x)
    for y in B:
        if y not in A:
            C.add(y)
    return C

def sunt_disjuncte(A, B):
    for x in A:
        if x in B:
            return False
    return True

def sterge_elemente(A, B):
    B = set(B)
    to_remove = set()
    for x in A:
        if x in B:
            to_remove.add(x)
    for x in to_remove:
        A.remove(x)

def produs_cartezian(A, B):
    C = set()
    for a in A:
        for b in B:
            C.add((a, b))
    return C
