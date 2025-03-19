import numpy as np
import functii as f
import zaux as s
import univers as univers

def main():
    print("introdu universul logic:")
    u = []
    #u = univers.citireUnivers()
    u = range(-2, 3, 1)
    logic = False
    lista_valori = []

    print("a) ∃yQ(5, y) ")
    logic, lista_valori = f.a(u)
    print("v(a) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

    print("b) ∃xQ(x,4) ")
    logic, lista_valori = f.b(u)
    print("v(b) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

    print("c) ∀x∃yQ(x, y) ")
    logic, lista_valori = f.c(u)
    print("v(c) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

    print("d) ∀y∃xQ(x, y)")
    logic, lista_valori = f.d(u)
    print("v(d) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

    print("e) ∃y∀xQ(x, y)")
    logic, lista_valori = f.e(u)
    print("v(e) = ", end = ""), print(logic)
    if logic :
        print("lista_valori = ", end = ""), print(lista_valori)
    s.spatiere()

if __name__ == '__main__':
    main()
