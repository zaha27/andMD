from propozitii import a, b, c, d

def test_propozitii():
    print("Propozitia a) Produsul a doi intregi negativi este pozitiv.")
    for x in range(-10, 11):
        for y in range(-10, 11):
            if a(x, y):
                print(f"  Adevărat pentru: ({x}, {y})")

    print("\nPropozitia b) Media a doi intregi pozitivi este pozitiva.")
    for x in range(-10, 11):
        for y in range(-10, 11):
            if b(x, y):
                print(f"  Adevărat pentru: ({x}, {y})")

    print("\nPropozitia c) Diferenta a doi intregi negativi nu este in mod necesar negativa.")
    for x in range(-10, 11):
        for y in range(-10, 11):
            if c(x, y):
                print(f"  Adevărat pentru: ({x}, {y})")

    print("\nPropozitia d) Valoarea absoluta a sumei nu depaseste suma valorilor absolute.")
    for x in range(-10, 11):
        for y in range(-10, 11):
            if d(x, y):
                print(f"  Adevărat pentru: ({x}, {y})")

if __name__ == "__main__":
    test_propozitii()
