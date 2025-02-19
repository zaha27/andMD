import vector as V

def cmmdc(a:int, b:int) -> int:
    while b:
        a, b = b, a%b
    return a

def factorial(n:int) -> int:
    if n == 0 :
        r = 1
    else :
        r =  n * factorial(n - 1)        
    return r

def factorialIt(n:int) -> int:
    f = 1
    for i in range(1, n+1) :
        f = f * i
    return f

def power(n:int, k:int) -> int:
    if k == 1 :
        return n 
    else :
        r = n * power(n, k - 1) 
    return r
        
def fibo(n:int) -> int:
    if n == 1 : 
        r = 1
    elif n == 2 :
        r = 2
    else :
        r = fibo(n - 1) + fibo(n - 2)
    return r

def aranjamente(n:int, k:int) -> int:
    if k == 0 :
        r = n
    else :
        r = (n - k) * aranjamente(n, k-1) 
    return r

#tema 2 problema 2
def dotproduct(n:int, v1:list, v2:list) -> int:
    if n == 1 : 
        r = v1[n] * v2[n]
    else : 
       r = r + dotproduct(n - 1, v1, v2)

