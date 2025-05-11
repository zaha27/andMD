import numpy as np # type: ignore
import functii as f
import zaux as s
import univers as univers

def main():
    u1 = []
    u2 = []
    u3 = []
    #print("introdu universul logic:")
    #u = univers.citireUnivers()
    u1 = range(-10, 11, 1)
    u2 = range(-100, 101, 1)
    u3 = np.arange(-10, 11, 0.1)

    logic = False
    lista_valori = []

    print("a. ∀x∃y(x^2 = y), x ∈ u1, y ∈ u2")
    logic, lista_valori = f.a(u1, u2)
    print("v(a) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

    print("b. ∀y∃x(x^2 = y), x ∈ u1, y ∈ u2")
    logic, lista_valori = f.a(u1, u2)
    print("v(a) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

if __name__ == '__main__':
    main()
