import expresii7
def e_tautologie_two(expresie):
    for p in [True, False]:
        for q in [True, False]:
            if not expresie(p, q):
                return False
    return True

def e_tautologie_three(expresie):
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                if not expresie(p, q, r):
                    return False
    return True

def e_contradictie_two(expresie):
    for p in [True, False]:
        for q in [True, False]:
            if expresie(p, q):
                return False
    return True

def e_contradictie_three(expresie):
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                if expresie(p, q, r):
                    return False
    return True

def e_neither_two(expresie):
    if(not e_contradictie_two(expresie) and not e_tautologie_two(expresie)) :
        return True
    return False

def e_neither_three(expresie):
    if(not e_contradictie_two(expresie) and not e_tautologie_three(expresie)) :
        return True
    return False


def determinare(expresie, number) :
    if number == 2 :
        if e_contradictie_two(expresie):
            print("contradictie")
            return
        elif e_tautologie_two(expresie):
            print("tautologie")
            return 
        elif e_neither_two(expresie):
            print("nici tautologie nici contradictie")
            return
        else :
            print("nedeterminare")
            return 
    elif number == 3: 
        if e_contradictie_three(expresie):
            print("contradictie")
            return
        elif e_tautologie_three(expresie):
            print("tautologie")
            return 
        elif e_neither_three(expresie):
            print("nici tautologie nici contradictie")
            return
        else :
            print("nedeterminare")
            return 
    return 

def print_type() :
    determinare(expresii7.i, 3)
    determinare(expresii7.ii, 3)
    determinare(expresii7.iii, 2)

        
