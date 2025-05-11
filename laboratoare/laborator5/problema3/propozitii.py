import predicate as pd

def a(U, nrLaturi):
    for i in range(len(U)):
        if pd.Q(U[i]) and nrLaturi[i] >= 2:
            print(f"a) Adevarat – {U[i]} este triunghi cu cel putin doua laturi egale")
            return True
    print("a) Fals – niciun triunghi nu are cel putin doua laturi egale")
    return False

def b(U, nrLaturi):
    for i in range(len(U)):
        if nrLaturi[i] >= 2 and not pd.R(U[i]):
            print(f"b) Fals – {U[i]} are cel putin doua laturi egale dar nu este dreptunghi")
            return False
    print("b) Adevarat – toate poligoanele cu cel putin doua laturi egale sunt dreptunghiuri")
    return True

def c(U, nrLaturi):
    for i in range(len(U)):
        if pd.R(U[i]) and pd.S(U[i]):
            print(f"c) Adevarat – {U[i]} este atat dreptunghi cat si patrat")
            return True
    print("c) Fals – niciun dreptunghi nu este si patrat")
    return False

def d(U, nrLaturi):
    for i in range(len(U)):
        if pd.S(U[i]) and nrLaturi[i] < 2:
            print(f"d) Fals – {U[i]} este patrat dar are mai putin de doua laturi egale")
            return False
    print("d) Adevarat – toate patratele au cel putin doua laturi egale")
    return True
