import predicate as pd

def a(U, nrLaturi) :
    for i in range(5):
        if pd.Q(U[i]) == True :
            if nrLaturi[i] > 2 :
                return True
    return False

def b(U, nrLaturi) :
    for i in range(5) :
        if nrLaturi[i] > 2 and not pd.R(U[i]):
            return False
    return True

def c(U, nrLaturi) :
    for i in range(5) :
        if pd.R(U[i]) and pd.S(U[i]) : 
            return True
    return False     

def d(U, nrLaturi) :
    for i in range(5) :
        if pd.S(U[i]) and nrLaturi[i] < 2 :
            return False
    return True



        