import pengelolaan

def reservasi_():
    ambil = pengelolaan.akses()
    antrian = ambil[2]
    try:
        if antrian == []:
            no = 1
        else:
            no = antrian[-1]["antrian"] + 1
    except KeyError, IndexError: 
        no = 1
    nama = input("Reservasi atas nama: ")
    data = {"nama": nama.title(), "antrian": no}
    antrian.append(data)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": antrian, "pesanan": ambil[3]}
    pengelolaan.Save(simpan)

def tampilkan_antrian():
    data = pengelolaan.akses()
    antrian = data[2]
    print("Antrian saat ini: ")
    no = 1
    for x in antrian:
        print(f"[Antrian {no}] {x["nama"]}")
        no += 1

def bersihkan_antrian():
    ambil = pengelolaan.akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [], "pesanan": ambil[3]}
    pengelolaan.Save(simpan)

def pesenan_selesai():
    ambil = pengelolaan.akses()
    antrian = ambil[2]
    antrian.pop(0)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": antrian, "pesanan": ambil[3]}
    pengelolaan.Save(simpan)

    
