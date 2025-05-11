def pcta(a, b, c) :
    for a in [False, True] :
        for b in [False, True] :
            for c in [False, True] :
                if (not a or b and c) and not b :
                    if a : return False
    return True

def pctb(p, q, s, r) :
    for p in [False, True] :
        for q in [False, True] :
            for s in [False, True] :
                for r in [False, True] :
                    if(not s and r) :
                        if not(p and q) and not r :
                            if s and (q and r) :
                                if p:
                                    if not q:
                                        return False
    return True


def main() :



    return

if __name__ == '__main__' :
    main()