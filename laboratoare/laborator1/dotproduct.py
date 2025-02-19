import functii as f
import vector as V

def main():
    n = 5
    v1 = []
    v2 = []

    V.citireLista1(v1, n)
    V.citireLista1(v2, n)  

    print("Produsul scalar este: ")
    print(f.dotproduct(n, v1, v2))

if __name__ == '__main__': 
    main()
