from functools import reduce
from functions import citire

def main():
    n = int(input("nr elemente: "))
    u = []
    v = []

    u = citire(n)
    v = citire(n)
    
    p = list(map(lambda x, y : x * y, u, v))
    ps = reduce(lambda x, y: x + y, p)

    s = list(map(lambda x, y: x + y, u, v))

    print("Produsul scalar:", ps)
    print("Vectorul suma:", s)

if __name__ == "__main__":
    main()
