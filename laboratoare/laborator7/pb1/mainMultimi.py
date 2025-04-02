import functiiMultimi as f

def main():
    A_input = input("Introduceti elementele multimii A: ")
    B_input = input("Introduceti elementele multimii B: ")

    A = set(A_input)
    B = set(B_input)

    print("A = ", A)
    print("B = ", B)

    print("Reuniunea", f.reuniune(A, B))
    print("Diferenta", f.diferenta(A, B))
    print("Diferenta simetrica", f.diferenta_simetrica(A, B))
    print("Sunt disjuncte?", f.sunt_disjuncte(A, B))
    print("Stergere elemente 1 2 3 din A", f.sterge_elemente(A, [1, 2, 3]))
    print("Produs cartezian:", f.produs_cartezian(A, B))

if __name__ == "__main__":
    main()
