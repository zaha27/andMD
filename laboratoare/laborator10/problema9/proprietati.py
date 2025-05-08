#from laborator3.oplogic import implicatie

def implicatie2(p, q):
    if p:
        return q
    else:
        return True

def reflexivitatea(matrix, n) :
    for i in range(n) :
        if matrix[i][i] != 1 :
            return False
    return True

def antireflexivitatea(matrix, n) :
    for i in range(n) :
        if matrix[i][i] != 0 :
            return False
    return True

def simetria(matrix, n) :
    for i in range(n) :
        for j in range(n) :
            if matrix[i][j] != matrix[j][i] :
                return False
    return True

def asimetria(matrix, n):
    for i in range(n):
        if matrix[i][i] != 0:
            return False
        for j in range(n):
            if matrix[i][j] == 1 and matrix[j][i] == 1:
                return False
    return True

def antisimetria(matrix, n):
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != matrix[j][i] and matrix[i][j] and matrix[j][i]:
                return False
    return True

def tranzitiva(matrix, n): 
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if not(implicatie2(matrix[j][k], matrix[i][k])):
                        return False
    return True