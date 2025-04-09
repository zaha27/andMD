from functools import reduce
from functions import citire

def main():
    u = []
    u = citire(7)

    nr_elemente_nule = len(list(filter(lambda x: x == 0, u)))
    nr_elemente_pozitive = len(list(filter(lambda x: x > 0, u)))
    nr_elemente_negative = len(list(filter(lambda x: x < 0, u)))

    print(nr_elemente_negative)
    print(nr_elemente_nule)
    print(nr_elemente_pozitive)

if __name__ == "__main__":
    main()
