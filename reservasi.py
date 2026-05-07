import database_resto

def reservasi_():
    ambil = database_resto.akses()
    antrian = ambil[2]
    try:
        if antrian == []:
            no = 1
        else:
            no = antrian[-1]["antrian"] + 1
    except KeyError, IndexError: 
        no = 1
    nama = input("Reservasi atas nama: ")
    data = {"nama": nama, "antrian": no}
    antrian.append(data)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": antrian, "pesanan_siapa": ambil[3]}
    database_resto.Save(simpan)

def tampilkan_antrian(antrian):
    data = database_resto.akses()
    antrian = data[2]
    print("Antrian saat ini: ")
    no = 1
    for x in antrian:
        print(f"[Antrian {no}] {x["nama"]}")
        no += 1

def bersihkan_antrian():
    ambil = database_resto.akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [], "pesanan_siapa": ambil[3]}
    database_resto.Save(simpan)

def pesenan_selesai():
    ambil = database_resto.akses()
    antrian = ambil[2]
    antrian.pop(0)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": antrian, "pesanan_siapa": ambil[3]}
    database_resto.Save(simpan)

    
