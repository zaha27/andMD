def cmmdc(a, b) :
    if(b == 0) :
        return a
    else :
        return cmmdc(b, a%b)

def a(i, j, L) :
    if(i == j) :
        L.append((i,j))

def b(i, j, L) :
    if((i + j) == 4) :
        L.append((i,j))

def c(a, b, L) :
    if(a > b) :
        L.append((a, b))

def d(a, b, L) :
    if b == 0 : return
    if(a % b == 0) :
        L.append((a, b))

def e(i, j, L) :
    if j == 0 : return
    if(cmmdc(i, j) == 1) :
        L.append((i, j))

def f(i, j, L) :
    if j == 0 : return 
    if(cmmdc(i, j) == 2) :
        L.append((i, j))