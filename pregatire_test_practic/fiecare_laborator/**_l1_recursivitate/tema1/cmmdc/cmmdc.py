def cmmdc(a, b) :
    if b == 0 :
        return a
    else :
        return cmmdc(b, a % b)