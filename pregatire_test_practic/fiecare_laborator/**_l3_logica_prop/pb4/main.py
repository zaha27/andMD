import functions as f

def main() :
    u = [False, True]
    print(f"{' ':<4}{'F':<5}{'B':<5}{'S':<5}{'Decl B':<10}{'Decl F':<10}{'Decl S':<10}")
    for florin in u :
        for bogdan in u :
            for stan in u :
                decl1 = f.declaratie_bogdan(florin, bogdan, stan)
                decl2 = f.declaratie_florin(florin, bogdan, stan) 
                decl3 = f.declaratie_stan(florin, bogdan, stan)
                f.print_tabel(florin, bogdan, stan, decl1, decl2, decl3)
    return

if __name__ == "__main__" :
    main()
