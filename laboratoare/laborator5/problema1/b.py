import numpy as np
import predicat as p

def b() :
    for i in range(-2,2,1) :
        rezultat = p.Q(i,4)
        if rezultat != 0 :
            return 1
    return 0



