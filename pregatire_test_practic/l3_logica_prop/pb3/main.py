import expresii as exp

def main() :
    print(f"    {'p':<10} {'q':<10} {'i_unu':<12} {'i_doi':<12}")
    p, q = False, False
    for p in [False, True] :
        for q in [False, True] :
            if exp.i_unu(p, q) == exp.i_doi(p, q) :
                print(f"****{p:<12} {q:<14} {exp.i_unu(p, q):<16} {exp.i_doi(p, q):<16}")
            else :
                print(f"{p:<14} {q:<14} {exp.i_unu(p, q):<16} {exp.i_doi(p, q):<16}")
    return

if __name__ == "__main__" :
    main()