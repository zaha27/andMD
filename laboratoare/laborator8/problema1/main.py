import functions as funct

def main ():

    A_one_1 = range(-10, 10, 1)
    A_one_2 = range(-10, 10, 1)
    A_one_3 = range(-10, 10, 1)
    A_two = range(-10, 10, 1)

    B_one = list(map(funct.g, A_one_1, A_one_2, A_one_3))
    B_two = list(map(lambda x: 2*x, A_two))

    print(B_two)
    print(B_one)

if __name__ == "__main__":
    main()