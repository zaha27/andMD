def citireLista(n) :
    v = []
    for i in range(n) :
        x = int(input())
        v.append(x)
    return v

def relatie(A, B) :
    E = []
    for a in A :
        for b in B :
            if a == 0 :
                print('nu se poate imparti la 0')
                continue
            elif b % a == 0:
                E.append((a, b))
    return E