import json


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
       pesanan_siapa = data["pesanan_siapa"]
    except KeyError: pesanan_siapa = []
    return [menu, stok_bahan, antrian, pesanan_siapa]

