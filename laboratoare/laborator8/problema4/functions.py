def citire(n) :
    vector = []
    for i in range(n) :
        x = float(input())
        vector.append(x)

    return vector

def max(a, b) :
    return a if a > b else b
