import functions as f

def main() :
    x = [1, 2, 3]
    y = [3, 2, 1]
    len = 3
    rez = f.produs_scalar(x, y, len)
    print(f"Produsul scalar a vectorilor x:{x} si y:{y} este -> {rez}")
    return

if __name__ == "__main__" :
    main()