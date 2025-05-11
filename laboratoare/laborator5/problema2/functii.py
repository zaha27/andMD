import predicat as p

def a(u1, u2) :      #a. ∀x∃y(x^2 = y), x ∈ u1, y ∈ u2
    logic = False
    listaRezultate = []
    for i in u1 :
        for j in u2 :
            if p.q1(i, j) :
                logic = True
                listaRezultate.append((i, j))
    return logic, listaRezultate

def b(u1, u2) :      #b. ∀x∃y(x^2 = y), x ∈ u1, y ∈ u2
    logic = False
    listaRezultate = []
    for i in u1 :
        for j in u2 :
            if p.q1(i, j) :
                logic = True
                listaRezultate.append((j, i))
    return logic, listaRezultate