import laboratoare.laborator3.oplogic as f

def main():
    print("%10s %10s %11s" % ('p', 'q', 'p and q'))
    for p in (False, True):
        for q in (False, True):
            rezultat = f.sau_exclusiv(p, q)
            print ("%10s %10s %10s" % ( p, q, rezultat))
if __name__ == '__main__':
    main()
