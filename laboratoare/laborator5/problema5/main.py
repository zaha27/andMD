def a(M, T) :
    for i in range(4) :
        if M[0][i] :
            return False 
    if T[0][1] :
        return False 
    return True

def b(M) :
    for i in range(4) :
        if M[i][i] :
            return True
    return False

def c(U, M, T) :
    for i in range(4) :
        ok = 1
        for j in range(4) :
                if not M[i][j] or not T[i][j] :
                    ok = 0
        if not ok :
            print(U[i])
            return True        
    return False

def d(M, T) :
    for i in range(4) :
        for j in range(4) :
            if M[i][j] == T[j][i] and M[i][j] == 1 :
                return True
    return False

def e(U, M, T) :
    nr = 0
    for i in range(4) :
        ok = 1
        for j in range(4) :
                if not M[i][j] or not T[i][j] :
                    ok = 0
        if not ok :
            print(U[i])
            nr = nr + 1

    return nr == 2

def f(M) :
    for i in range(4) :
        nr = 0
        for j in range(4) :
            if M[i][j] :
                nr = nr + 1
        if nr == 2 : return True
    return False

def g(M, T) :
    for i in range(4) :
        nr = 0
        for j in range(4) :
            if M[i][j] :
                nr = nr + 1
        if nr == 1 : return True
    return False

def main() :
    U = ['Ana', 'Maria', 'Ion', 'George']

    M = [[0,0,0,1], 
         [1,0,1,0], 
         [1,1,1,1], 
         [1,0,0,0]]
    
    T = [[0,0,1,0], 
         [0,0,1,0], 
         [1,1,0,1], 
         [0,1,0,0]]

    

