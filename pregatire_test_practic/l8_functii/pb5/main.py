import functions as f

def main() :
    LW = []
    n = 0
    LW = f.citire_lista_cuvinte(n)
    print(f"LW : {LW}")
    print(f"lista cu majuscule: {f.majuscule(LW)}")
    print(f"concatenarea listei : {f.concatenare(LW)}")
    return

if __name__ == "__main__" :
    main()
