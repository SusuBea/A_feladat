import random
vel_lista = []

def vel_sorozat():
    vel_szoveg = ""
    i = 0
    while i <= 11:
        vel = int(random.random() * 1011) - 10
        vel_lista.append(vel)
        if i == 11:
            vel_szoveg += str(vel)
        else:
            vel_szoveg += str(vel) + "$"
        i += 1
    print("II/A,B,C: ")
    print(f"\t {vel_szoveg}")

def paratlanok_szama():
    i = 0
    paratlan_db = 0
    while i < len(vel_lista):
        if vel_lista[i] % 2 == 1:
            paratlan_db += 1
        i += 1
    return paratlan_db

def konzol_kiir():
    print("II/D,E: ")
    print(f"\t a páratlanok száma: {paratlanok_szama()} ")

def fajlba_kiir():
    fajlom = open("eredmeny.txt", "w", encoding="utf-8")
    fajlom.write(f"kimutatas.txt tartalma: \nII/F: \n \t A páratlanok száma: {paratlanok_szama()}.")
    fajlom.close()









