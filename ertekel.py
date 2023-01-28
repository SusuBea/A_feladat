def beker():
    etel = input("Étel neve: ")
    rendelo_szemely = input("Étel rendelőjének a neve: ")
    ertekeles = int(input("Értékelés (1-5): "))

    if ertekeles < 0:
        print("Az értékelés nem lehet negatív.")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható.")
    else:
        print("Köszönjük az értékelést!")

    print("I/A,B: ")
    print(f"\t Étel neve: {etel}")
    print(f"\t Étel rendelőjének neve: {rendelo_szemely}")
    print("I/C: ")
    print(f"\t Értékelés (1-5): {ertekeles}")



