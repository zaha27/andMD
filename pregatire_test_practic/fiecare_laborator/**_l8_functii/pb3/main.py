from functii import citire_vector
import functools as f
import math as m

def main() :
    n = 5
    u = citire_vector(n, 1, 'u')
    v = citire_vector(n, 2, 'v')

    f = lambda x, y: x * y
    rezultate = map(f, (u, v))


if __name__ == '__main__':
    main()