import laboratoare.laborator3.oplogic as f

def main():
    print("Tabel de Adevar: \n")
    print("%10s %10s %10s %10s %10s %10s" % ('Bogdan', 'Florin', 'Stan', 'Decl B', 'Decl S', 'Decl F'))
    for bogdan in (False, True):
        for florin in (False, True):
            for stan in (False, True):
                declBogdan = stan and not(florin)    
                declStan = f.implica(bogdan, florin) 
                declFlorin = not(florin) and (bogdan or florin)
                vinovatie = declBogdan and declStan and declFlorin
                if not(vinovatie):
                    print("%10d %10d %10d %10d %10d %10d" % (bogdan, florin, stan, declBogdan, declFlorin, declStan))
                else: 
                    print ("***%7d %10d %10d %10d" % ( bogdan, florin, stan, declBogdan, declFlorin, declStan))


    for bogdan in (False, True):
        for florin in (False, True):
            for stan in (False, True):
                declBogdan = stan and not(florin)    
                declStan = f.implicatie(bogdan, florin) 
                declFlorin = not(florin) and (bogdan or florin)

                if declBogdan and declStan and declFlorin:
                    print("%10s %10s %10s %10s %10s %10s" % (bogdan, florin, stan, declBogdan, declStan, declFlorin))
                    print("\nVinovati:")
                    if bogdan : 
                        print("Vinovat")
                    else :
                        print("Nevinovat")
                    if stan :
                        print("Vinovat")
                    else :
                        print("Nevinovat")
                    if florin :
                        print("Vinovat")
                    else : 
                        print("Nevinovat")
        
if __name__ == '__main__':
    main()

