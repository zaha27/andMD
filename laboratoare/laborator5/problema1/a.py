import numpy as np
import predicat as p

def a() :
    for i in range(-2,2,1) :
        rezultat = p.Q(5,i)
        if rezultat != 0 :
            return 1
    return 0



