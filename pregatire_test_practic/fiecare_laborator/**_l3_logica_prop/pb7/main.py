import determinari as d
import functii as f

def main() :
    lista = [
        ('i', f.i, 3),
        ('ii', f.ii, 3),
        ('iii', f.iii, 2),
    ]
    for nume, arg, nr_parametri in lista :
        print(f"Functia {nume} este", end =" ")
        if d.tautologie(arg, nr_parametri) == 1 :
            print(f"tautologie")
        elif d.contradictie(arg, nr_parametri) == 1 :
            print(f"contradictie")
        else :
            print(f"nici tautologie nici contradictie")

if __name__ == "__main__" :
    main()