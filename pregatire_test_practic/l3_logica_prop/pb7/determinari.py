import functii as f

def tautologie(f_arg, cati_parametri) :
    u = [False, True]
    if cati_parametri == 2 :
        for p in u :
            for q in u :
                if f_arg(p, q) == False :
                    return False
        return True
    elif cati_parametri == 3 :
        for p in u :
            for q in u :
                for r in u :
                    if f_arg(p, q, r) == False :
                        return False
        return True  

def contradictie(f_arg, cati_parametri) :
    u = [False, True]
    if cati_parametri == 2 :
        for p in u :
            for q in u :
                if f_arg(p, q) == True :
                    return False
        return True
    elif cati_parametri == 3 :
        for p in u :
            for q in u :
                for r in u :
                    if f_arg(p, q, r) == True :
                        return False
        return True      
