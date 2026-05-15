import json
import time


hari = 1

def Cek(pesan, eror):
    while True:    
        try:
            x = int(input(pesan))
            break
        except ValueError: print(eror)
    return x


def Save(simpan):
    with open("data_resto.json", "w") as f:
        json.dump(simpan, f)


def Open():
    with open("data_resto.json", "r") as f:
        loaded = json.load(f)
    return loaded


def akses():
    data = Open()
    try:
        menu = data["Menu"]
    except KeyError: menu = []
    try:
        stok_bahan = data["stok_bahan"]
    except KeyError: stok_bahan = []     
    try:
        antrian = data["antrian"]      
    except KeyError: antrian = []
    try:
        pesanan = data["pesanan"]
    except KeyError: pesanan = []
    return [menu, stok_bahan, antrian, pesanan]


def operasional():
    tutup = False
    global hari
    while tutup == False:
        print("\n===============================================================")
        print(f"[Hari ke-{hari}]")
        print("Buka!")
        print("[Jam] 07:00")
        time.sleep(5)
        print("\n[Jam] 12:00")
        time.sleep(5)
        print("\n[Jam] 17:00")
        time.sleep(5)
        print("\n[Jam] 22:00")
        print("Tutup!")
        tutup = True
    time.sleep(60)
    hari += 1
    tutup = False
    operasional()