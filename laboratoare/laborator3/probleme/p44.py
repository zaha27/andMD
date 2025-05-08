from itertools import product

def implica(p, q):
    return not p or q

def main():
    print("Tabel de Adevăr:\n")
    print("%10s %10s %10s %10s %10s %10s" % ('Bogdan', 'Florin', 'Stan', 'Decl B', 'Decl S', 'Decl F'))
    print("-" * 70)
    
    for bogdan, florin, stan in product([False, True], repeat=3):
        declBogdan = stan and not florin
        declStan = implica(bogdan, florin)
        declFlorin = not florin and (bogdan or stan)
        
        if declBogdan and declStan and declFlorin:
            print("%10s %10s %10s %10s %10s %10s" % (bogdan, florin, stan, declBogdan, declStan, declFlorin))
            print("\nSoluția corectă:")
            print(f"Bogdan: {'Vinovat' if bogdan else 'Nevinovat'}")
            print(f"Florin: {'Vinovat' if florin else 'Nevinovat'}")
            print(f"Stan: {'Vinovat' if stan else 'Nevinovat'}")
            return

if __name__ == '__main__':
    main()

