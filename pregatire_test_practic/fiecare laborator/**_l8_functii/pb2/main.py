import functools as f
import math as m

def main() :
    x = (3.14, -23.23, -123.82, 82, -96)
    pozitive = filter(lambda x: x > 0, x)
    rezultat = map(lambda x: m.sqrt(x), pozitive)
    print(list(rezultat))

    return


if __name__ == '__main__':
    main()