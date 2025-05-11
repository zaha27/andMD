def a(x, y):
    return x < 0 and y < 0 and x * y > 0

def b(x, y):
    return x > 0 and y > 0 and (x + y) / 2 > 0

def c(x, y):
    return x < 0 and y < 0 and (x - y >= 0)

def d(x, y):
    return abs(x + y) <= abs(x) + abs(y)