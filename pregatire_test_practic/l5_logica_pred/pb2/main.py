import numpy as np #type: ignore
import predicate as pd
import propozitii as exp

def main():
    # Universuri
    U1 = list(range(-10, 11))
    U2 = list(range(-100, 101))
    U3 = np.arange(-10.0, 10.1, 0.1)

    print("a) ∀x∈U1 ∃y∈U2 : x² = y")
    rezultat = exp.a(None, None, U1, U2)
    if rezultat:
        print("  ⇒ Adevărat. Exemple:", rezultat[:5], "...")
    else:
        print("  ⇒ Fals.")

    print("\nb) ∀y∈U2 ∃x∈U1 : x² = y")
    rezultat = exp.b(None, None, U1, U2)
    if rezultat:
        print("  ⇒ Adevărat. Exemple:", rezultat[:5], "...")
    else:
        print("  ⇒ Fals.")

    print("\nc) ∃x∈U3 ∀y∈U3 : x·y = 1")
    rezultat = exp.c(None, None, U3)
    if rezultat:
        print("  ⇒ Fals. Contraexemple:", rezultat[:5], "...")
    else:
        print("  ⇒ Adevărat.")

    print("\nd) ∀x∈U3 ∃y∈U3 : x·y = 1")
    rezultat = exp.d(None, None, U3)
    if rezultat:
        print("  ⇒ Adevărat. Exemple:", rezultat[:5], "...")
    else:
        print("  ⇒ Fals.")

if __name__ == "__main__":
    main()
