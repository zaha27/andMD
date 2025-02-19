def citireLista1( v:list, n:int ) :
    for i in range(0, n):
        print('v[%d] = ' % i, end =' ')
        x = int(input())
        v.append(x)
def citireLista2( v:list ) -> int:
    n = 0
    while True:
        try: 
            x = int(input('x = '))
            v.append(x)
            n = n + 1
        except EOFError: 
            print('\nAti terminat de introdus valorile! ')
            break
    return n