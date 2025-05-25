def main() :
    U={"MD","MS","F","PL","SD","MN","PC","ETH","ENG"}

    R={"MD","F","PL","ENG"}
    S={"MD","MS","PC","PL"}

    print(set(R & S))
    print(set(U - (R | S)))
    print(set(R - S))

    return

if __name__ == "__main__" :
    main()