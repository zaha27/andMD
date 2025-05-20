def p(p, q, r, s) :
    ok = 0
    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                for s in [False, True]:
                    if (not p and q) and (not s and r) and (p or q) and (q and r) :
                        ok = 1