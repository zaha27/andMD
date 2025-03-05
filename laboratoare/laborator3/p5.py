import oplogic as f

def main():
    print("Tabel de Adevar: \n")
    print("%10s %10s %10s %10s %10s" % ('Alexandru', 'Bianca', 'Carmen', 'Dan', 'Ela'))
    for alexandru in (False, True):
        for bianca in (False, True):
            for carmen in (False, True):
                for dan in (False, True):
                    for ela in (False, True):
                        expr1 =     
                        expr2 = 
                        expr3 = 
                        expr4 = 
                        expr5 = 
                        televizor = declBogdan and declStan and declFlorin
                if not(televizor):
                    print("%10d %10d %10d %10d %10d %10d %10d %10d %10d %10d" % (alexandru, bianca, carmen, dan, ela, expr1, expr2, expr3, expr4, expr5))
                else: 
                    print ("***%7d %10d %10d %10d %10d %10d %10d %10d %10d %10d" % (alexandru, bianca, carmen, dan, ela, expr1, expr2, expr3))


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

