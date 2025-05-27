def pb1_recursivitate(a : int, b : int) -> int :
    if b == 0 :
        return a
    return pb1_recursivitate(a%b, b)
