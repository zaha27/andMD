def a(M, T) :
    rez = not M[0][1] and not T[0][1]
    return rez

def b(M, T) :
    rez = 0
    for i in range(4) :
        if M[i][i] :
            rez = 1
            break
    return rez

def c(M, T) :
    for i in range(4) :
        ok = 0
        for j in range(4) :
            if not M[i][j] and not T[i][j] and i != j :
                ok = 1
        if ok == 0 : return True
    return False

def d(M, T) :
    for i in range(4) :
        for j in range(4) :
            if M[i][j] and T[j][i] :
                return True
    return False
    
def e(M, T) :
    nr = 0
    for i in range(4) :
        ok = 0
        for j in range(4) :
            if not M[i][j] and not T[i][j] and i != j :
                ok = 1
        if ok == 0 :
            nr = nr + 1
    return nr == 2

def f(M, T) :
    for i in range(4) :
        nr = 0
        for j in range(4) :
            if M[i][j] :
                nr = nr + 1
        if nr == 2 : return False
    return True

def g(M, T) :
    for i in range(4) :
        nr = 0
        for j in range(4) :
            if T[i][j] :
                nr = nr + 1
        if nr == 1 : return True
    return False

Univers = {
        'Ana' : 0, 
        'Maria' : 1,
        'Ion' : 2,
        'George' : 3
    }