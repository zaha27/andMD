def citireLista(v: list, n: int):
    for i in range(n):
        x = int(input(f'v2[{i}] = '))
        v.append(x)

def a(v: list, n: int) -> int:
    if n == 0: 
        return 0
    
    if v[n - 1] < 0:
        r = 1 + a(v, n - 1)
    else:
        r = a(v, n - 1)
    return r
    
def b(v: list, n: int) -> int:
    if n == 0: 
        return 1
    r = v[n - 1] * b(v, n - 1)  
    return r

def c(v: list, n: int) -> int:
    if n == 0: 
        return 1
    r = v[n - 1] + b(v, n - 1)  
    return r

def d(v: list, n: int) -> int:
    if n == 0: 
        return 1
    elif v[n - 1] < 0 :
        r = v[n - 1] * d(v, n - 1)  
    else :
        r = d(v, n - 1)  
    return r

#maxim
def e(v: list, n: int) -> int:
    if n == 1: 
        return v[0]
    
    max_rest = e(v, n - 1)
    
    return max(v[n - 1], max_rest)

def f(v: list, n: int) -> int:
    if n == 1: 
        return v[0]
    
    min_rest = f(v, n - 1)
   
    return min(v[n - 1], min_rest)
