import oplogic as f

def i(p, q, r):
    first = p or q
    second = not(p) or q
    third = q or r
    last = f.implica(second, third)
    return first and last

def ii(p, q, r):
    first = f.implica(p, q)
    second = f.implica(q, r)
    third = f.implica(p, r)
    last = f.implica(second, third)
    return first and last 

def iii(a, b):
    first = f.implica(b, a)
    second = f.biconditie(b, first) 
    last = f.implica(second, a)
    return last

