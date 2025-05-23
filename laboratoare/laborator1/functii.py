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
        r = (n - k + 1) * aranjamente(n, k-1) 
    return r

#tema 2 problema 2
def dotproduct(n: int, v1: list, v2: list) -> int:
    if n == 1: 
        return v1[0] * v2[0]  
    return v1[n-1] * v2[n-1] + dotproduct(n - 1, v1, v2)

def cmmdc_rec(a: int, b: int) -> int :
    if b == 0 :
        return a
    else :
        r = cmmdc_rec(b, a % b)
    return r

def cmmdc_vector(n: int, v: list) -> int :
    if n == 0 :
        return v[0]
    else :
        v[0] = cmmdc(v[0], v[n])
        cmmdc_vector(n - 1, v)
    return v[0]

def nrcifre(n: int) -> int:
    if n == 0 :
        return 0
    else :
        r = 1 + nrcifre(int(n / 10))
        #sau 
        #r = 1 + nrcifre(n // 10)
    return r

def produs_cifre(n: int) -> int:
    if n == 0 :
        return 1
    else :
        r = n%10 * nrcifre(int(n / 10))
        #sau 
        #r = n%10 + nrcifre(n // 10)
    return r