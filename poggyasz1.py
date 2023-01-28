from Poggyasz import Poggyasz
poggyasz_lista = []

def beolvasas():
    fajlom = open("csomag.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    print(fejlec)
    fajltartalom = fajlom.readlines()
    fajlom.close()
    adatfeldolgozas(fajltartalom)

def adatfeldolgozas(fajltartalom):
    i = 0
    while i < len(fajltartalom):
        sor = fajltartalom[i].strip().split("#")
        poggyasz = Poggyasz(sor)
        poggyasz_lista.append(poggyasz)
        i += 1
    print("III/A,B: ")
    print(f"\t A poggyászok száma: {len(poggyasz_lista)}")

def atlag_suly():
    i = 0
    db = 0
    suly = 0
    while i < len(poggyasz_lista):
        if poggyasz_lista[i].szelesseg == 51:
            db += 1
            suly += poggyasz_lista[i].suly
        i += 1

    atlag = int((suly / db) * 1000)
    print("III/C: ")
    print(f"\t Az 51 cm-es poggyászok átlag súlyértéke: {atlag} g")

def legmagasabb_poggyasz():
    i = 0
    legmagasabb = 0
    index = i
    while i < len(poggyasz_lista):
        if poggyasz_lista[i].magassag > legmagasabb:
            legmagasabb = poggyasz_lista[i].magassag
            index = i
        i += 1

    print("III/D: ")
    print(f"\t A legmagassabb poggyász méretei: {poggyasz_lista[index].szelesseg}x{poggyasz_lista[index].magassag}x{poggyasz_lista[index].melyseg}, súlya: {poggyasz_lista[index].suly}kg")












