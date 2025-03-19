import numpy as np
import predicat as p

def a(u) :
    logic = False
    listaRezultate = []
    for i in u :
        rezultat = p.Q(5,i)
        if rezultat != 0 :
            logic = True
            listaRezultate.append(i)
    return logic, listaRezultate

def b(u):
    logic = False
    listaRezultate = []
    for i in u:
        rezultat = p.Q(i, 4)
        if rezultat != 0:
            logic = True
            listaRezultate.append(i)
    return logic, listaRezultate

def c(u):
    logic = False
    listaRezultate = []
    for i in u:
        for j in u:
            if p.Q(i, j) != 0:
                logic = True
                listaRezultate.append((i, j))
    return logic, listaRezultate

def d(u):
    logic = False
    listaRezultate = []
    for j in u:
        for i in u:
            if p.Q(i, j) != 0:
                logic = True
                listaRezultate.append((j, i))
    return logic, listaRezultate

def e(u) :
    logic = False
    listaRezultate = []
    for i in u:
        for j in u:
            if p.Q(i, j) != 0:
                logic = True
                listaRezultate.append((i, j))
    return logic, listaRezultate
