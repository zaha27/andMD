def numar_cifre(n) :
    if n != 0 :
        return 1 + numar_cifre(n // 10)
    else :
        return 0
    
    
def main() :
    n = 123912
    rez = numar_cifre(n)
    print(f"numarul de cifre a numarului {n} este {rez}")

if __name__ == "__main__" :
    main()