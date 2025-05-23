import functions as f

def main() :
    lista_argumente_f = [
        ('i', f.i, 2), 
        ('ii', f.ii, 2), 
        ('iii', f.iii, 3),
        ('iv', f.iv, 3), 
        ('v', f.v, 2)
        ]
    for nume, arg, parametri in lista_argumente_f :
        print(f"Functia {nume}", end = " ")
        if not(f.tautologie(arg, parametri)) :
            print(f"nu", end = " ") 
        print(f"este tautologie")
    return

if __name__ == "__main__" :
    main()