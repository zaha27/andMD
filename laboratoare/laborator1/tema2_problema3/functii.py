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
    
