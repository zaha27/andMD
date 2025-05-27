import functions as f

def main() :
    u = [False, True]
    print(f"{' ':<4}{'A':<5}{'B':<5}{'C':<5}{'D':<5}{'E':<5}{'1':<5}{'2':<5}{'3':<5}{'4':<5}{'5':<5}")
    print(f"    ----------------------------------------------")
    #print(f"{for _ in range(10) : print('-', end = "")}")
    for a in u :
        for b in u :
            for c in u :
                for d in u :
                    for e in u :
                        decl1 = f.unu(a, b, c, d, e)
                        decl2 = f.doi(a, b, c, d, e)
                        decl3 = f.trei(a, b, c, d, e)
                        decl4 = f.patru(a, b, c, d, e)
                        decl5 = f.cinci(a, b, c, d, e)
                        f.print_tabel(a, b, c, d, e, decl1, decl2, decl3, decl4, decl5)                                     
    return

if __name__ == "__main__" :
    main()
