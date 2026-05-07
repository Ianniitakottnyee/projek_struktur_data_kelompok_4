import database_resto
import menu

ambil = database_resto.akses()
antrian = ambil[2]

def pesanan():
    ambil = database_resto.akses()
    kumpulan_pesanan = ambil[3]
    while True:
        siapa = input("Nama pemesan: ")
        for x in antrian:
            if x["nama"] == siapa:
                print(f"{x["nama"]} terdaftar dalam antrian")
                break
            else:
                print("Nama belum terdaftar di antrian")
        break

    x = database_resto.akses()
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
            print(f"Ditemukan: {hasil}")
        else:
            print("Menu tidak ditemukan")
        semua_pesanan.append(hasil)
        pesanan_siapa = {"nama": siapa, "pesanan": semua_pesanan}
        kumpulan_pesanan.append(semua_pesanan)
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": ambil[2], "pesanan_siapa": pesanan_siapa}
    database_resto.Save(simpan)

    x = database_resto.akses()
    print(x[3])


def bersihkan_pesanan():
    ambil = database_resto.akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [2], "pesanan_siapa": []}
    database_resto.Save(simpan)


