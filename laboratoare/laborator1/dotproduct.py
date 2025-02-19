import functii as f
import vector as V

def main():
    n = 5
    v1 = 0
    v2 = 0
    V.citireLista1(v1, n)
    V.citireLista2(v2, n)  

    print(f.dotproduct(5, v1,v2))

if __name__ == '__main__': 
    main()
