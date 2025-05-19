import predicate as pd

def a(x, y, U1, U2) : #VxEy
    lista = []
    for x in U1 :
        ok = 0
        for y in U2 :
            if pd.x_patrat_egal_y(x, y) == True :
                ok = 1
                lista.append((x,y))
        if ok == 0 : return False
    return lista

def b(x, y, U1, U2) : #VyEx
    lista = []
    for y in U2 :
        ok = 0
        for x in U1 :
            if pd.x_patrat_egal_y(x, y) == True :
                lista.append((x,y))
                ok = 1
        if ok == 0 : return False
    return lista

def c(x, y, U3) : #ExVy
    lista = []
    for x in U3 :
        ok = 0
        for y in U3 :
            if pd.x_ori_y_egal_1(x, y) == False :
                ok = 1
                lista.append((x,y))
        if ok == 0: 
            return lista
    return False

def d(x, y, U3) :
    lista = []
    for x in U3 :
        ok = 0
        for y in U3 :
            if pd.x_ori_y_egal_1(x, y) == True :
                ok = 1
                lista.append((x,y))
        if ok == 0 : return False
    return lista

