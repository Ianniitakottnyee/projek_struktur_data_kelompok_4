import menu
import reservasi
import pengelolaan
import alat_bantu
import pemesanan


while True:
    ambil = pengelolaan.akses()
    q = ambil[2]
    print("")
    print("================ kafe apa namanya =================")
    print("[1] Reservasi pelanggan")
    print("[2] Lihat menu")
    print("[3] Pemesanan")
    print("[4] Daftar Antrian")
    print("[5] Bersihkan antrian")
    try:
        print(f"[6] Pesanan atas nama {q[0]["nama"]} telah selesai")
    except IndexError, KeyError, TypeError:
        print(f"[6] Antrian pesanan kosong")



    mode = alat_bantu.Cek("Pilih: ", "Input harus berupa angka!")
    if mode == 1:
        reservasi.reservasi_()

    elif mode == 2:
        x = pengelolaan.akses()
        root = menu.build_tree("Menu", x[0])

        print("=== DAFTAR MENU ===")
        menu.tampilkan_tree(root)

    elif mode == 3:
        pemesanan.pesanan()
    elif mode == 4:
        reservasi.tampilkan_antrian()
    elif mode == 5:
        reservasi.bersihkan_antrian()
    elif mode == 6:
        reservasi.pesenan_selesai()