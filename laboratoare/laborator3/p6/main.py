import functii as f

def main():
    print("Punctul 1:")
    print("Este tautologie?" if f.e_tautologie_two(f.expresie1) else "NU este tautologie.")

    print("\nPunctul 2:")
    print("Este tautologie?" if f.e_tautologie_two(f.expresie2) else "NU este tautologie.")

    print("\nPunctul 3:")
    print("Este tautologie?" if f.e_tautologie_three(f.expresie3) else "NU este tautologie.")

    print("\nPunctul 4:")
    print("Este tautologie?" if f.e_tautologie_three(f.expresie4) else "NU este tautologie.")

    print("\nPunctul 5:")
    print("Este tautologie?" if f.e_tautologie_two(f.expresie5) else "NU este tautologie.")

if __name__ == "__main__":
    main()
