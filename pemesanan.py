import pengelolaan
import menu


def pesanan():
    ambil = pengelolaan.akses()
    antrian = ambil[2]
    kumpulan_pesanan = ambil[3]
    if antrian == []:
        print("Belum ada Antrian")
        return
    else:
        print("Daftar Antrian:")
        no = 1
        for x in antrian:
            print(f"{no}. {x["nama"]}")
            no += 1
    berhenti = False
    while berhenti == False:
        siapa = input("Atas nama: ")
        for x in antrian:
            if siapa.title() == x["nama"]:
                berhenti = True
                siapa = x["nama"]
                break
        else:
            print("Nama belum terdaftar di antrian")


    x = pengelolaan.akses()
    root = menu.build_tree("Menu", x[0])
    print("=== DAFTAR MENU ===")
    menu.tampilkan_tree(root)
    menu.index_tree(root)

    print("\n=== Pilih Pesanan ===")
    semua_pesanan = []
    while True:
        kode_dicari = input("kode menu: ")
        if kode_dicari == ".":
            break
        hasil = menu.index_menu.get(kode_dicari)
        if hasil:
            print(f"Ditemukan: {hasil["nama"].ljust(15)} Rp.{hasil["harga"]}")
            semua_pesanan.append(hasil["nama"])
        else:
            print("Menu tidak ditemukan")
    pesanan_siapa = {"nama": siapa, "pesanan": semua_pesanan}
    kumpulan_pesanan.append(pesanan_siapa)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": ambil[2], "pesanan": kumpulan_pesanan}
    pengelolaan.Save(simpan)



def bersihkan_pesanan():
    ambil = pengelolaan.akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [2], "pesanan": []}
    pengelolaan.Save(simpan)


