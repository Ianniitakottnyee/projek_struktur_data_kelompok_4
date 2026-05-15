import menu
import reservasi
import pengelolaan
import pemesanan
import dapur_
import deliveri
import threading

tutup = False

t = threading.Thread(target=pengelolaan.operasional)
t.start()

while True:
    ambil = pengelolaan.akses()
    q = ambil[2]
    print("")
    print("================ kafe apa namanya =================")
    print("[1] Reservasi Pelanggan")
    print("[2] Lihat Menu")
    print("[3] Pemesanan")
    print("[4] Daftar Antrian")
    print("[5] Bersihkan Antrian")
    try:
        print(f"[6] Pesanan atas nama {q[0]["nama"]} telah selesai")
    except IndexError, KeyError, TypeError:
        print(f"[6] Antrian pesanan kosong")
    print("[7] Antrian Dapur")
    print("[8] Tambahkan Lokasi")
    print("[9] Antar Pesanan")
    print("[10] Tampilkan Peta")



    mode = pengelolaan.Cek("Pilih: ", "Input harus berupa angka!")
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
    elif mode == 7:
        dapur_.tampilkan_dapur()
    elif mode == 8:
        deliveri.tambah_jalan()
    elif mode == 9:
        deliveri.pengantaran()
    elif mode == 10:
        deliveri.peta()