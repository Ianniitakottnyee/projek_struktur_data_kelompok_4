import menu
import reservasi
import database_resto
import alat_bantu
import pemesanan


while True:
    ambil = database_resto.akses()
    q = ambil[2]
    print("================ kafe apa namanya =================")
    print("[1] Reservasi")
    print("[2] Lihat menu")
    print("[3] Pemesanan")
    print("[4] Antrian")
    print("[5] Bersihkan antrian")
    try:
        print(f"[6] Pesanan atas nama {q[0]["nama"]} telah selesai")
    except IndexError, KeyError, TypeError:
        print(f"[6] Antrian pesanan kosong")



    mode = alat_bantu.Cek("Pilih: ", "Input harus berupa angka!")
    if mode == 1:
        reservasi.reservasi_()

    elif mode == 2:
        x = database_resto.akses()
        root = menu.build_tree("Menu", x[0])

        print("=== DAFTAR MENU ===")
        menu.tampilkan_tree(root)

        menu.index_tree(root)

        print("\n=== CARI MENU ===")
        kode_dicari = input("kode menu: ")

        hasil = menu.index_menu.get(kode_dicari)
        if hasil:
            print(f"Ditemukan: {hasil}")
        else:
            print("Menu tidak ditemukan")

    elif mode == 3:
        pemesanan.pesanan()
    elif mode == 4:
        ambil = database_resto.akses()
        reservasi.tampilkan_antrian(ambil[2])
    elif mode == 5:
        reservasi.bersihkan_antrian()
    elif mode == 6:
        reservasi.pesenan_selesai()