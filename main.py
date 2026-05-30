import threading
import os

import shared
import pengelolaan
import pemesanan
import reservasi
import deliveri
import dapur_
import gudang
import menu

shared.memasak = dapur_.KitchenQueue()
dapur_.set_dapur(shared.memasak)
shared.penyimpanan = gudang.Gudang()
hidangan = menu
waktu_program = shared.waktu_program


''' MENU UTAMA CAFE '''
def tampilkan_menu_utama():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================")
    print("============ Cs.in Cafe ============")
    print("====================================") 
    print(f"Jam Sekarang: {waktu_program['jam']:02d}:{waktu_program['menit']:02d}")
    print("------------------------------------")
    print("Status: BUKA")
    print("Selamat datang di Cs.in Cafe🍜")
    print("====================================")
    ambil = pengelolaan.akses()
    q = ambil[2]
    print("[1] Reservasi Pelanggan")
    print("[2] Lihat Menu")
    print("[3] Antrian Dapur")
    print("[4] Pesan antar")
    print("[5] Peta")
    print("[6] Daftar pengunjung hari ini")
    print("[7] Tampilkan stok gudang")

    print("====================================")
    if shared.diproses is not None:
        shared.log_queue.put("\033[91m" + f"[Dapur] Pesanan #{shared.diproses.nomor} atas nama {shared.diproses.nama} sedang diproses" + "\033[0m")
    elif shared.log_queue.empty():
        shared.log_queue.put(f"[Dapur] Istirahat...")
    pengelolaan.mulai()
    print("====================================\n")

    mode = pengelolaan.Cek("Pilih: ", "Input harus berupa angka!")
    if mode == 0:
        ...

    elif mode == 1:
        siapa = reservasi.reservasi_()
        pemesanan.pesanan(siapa)
        input("\nTekan enter untuk keluar...")

    elif mode == 2:
        x = pengelolaan.akses()
        root = hidangan.build_tree("Menu", x[0])

        print("=========== DAFTAR MENU ===========")
        hidangan.tampilkan_tree(root)
        input("\nTekan enter untuk keluar...")

    elif mode == 3:
        shared.memasak.tampilkan_antrean()
        input("\nTekan enter untuk keluar...")

    elif mode == 4:
        ...
        deliveri.pengantaran()
        input("\nTekan enter untuk keluar...")

    elif mode == 5:
        print(" [1] Tambahkan lokasi baru.")
        print(" [2] Lihat peta")
        pilih = pengelolaan.Cek("Pilihan: ", "Input tidak valid.")
        if pilih == 1:
            deliveri.tambah_jalan()
        elif pilih == 2:
            deliveri.peta()
        input("\nTekan enter untuk keluar...")

    elif mode == 6:
        reservasi.tampilkan_pengunjung()
        input("\nTekan enter untuk keluar...")

    elif mode == 7:
        shared.penyimpanan.tampilkan_stok()
        input("\nTekan enter untuk keluar...")

    elif mode == 11:
        exit()

    elif mode == -1:
        pengelolaan.reset()

''' MENU SAAT TUTUP '''
def tampilkan_layar_terkunci():
    global waktu_program
    waktu_program["jam"] = waktu_program["jam"] % 24
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================")
    print("      Toko / Layanan Sedang Tutup   ")
    print("====================================")
    print(f"Jam Sekarang: {waktu_program['jam']:02d}:{waktu_program['menit']:02d}")
    print("------------------------------------")
    print("Status: MENU UTAMA TIDAK DAPAT DIAKSES")
    print("Jam Operasional: 07:00 s/d 22:00")
    print("====================================")
    print("Tekan ENTER untuk cek waktu atau 'exit' untuk keluar.")
    print("Ketik /skip untuk tidur.")
    pilihan = input(">> ").lower()
    if pilihan == "exit":
        waktu_program["berjalan"] = False
        exit()
    elif pilihan == "/skip":
        pengelolaan.reset()
'''
====================================================================================================================================================
|                                                                   PROGRAM UTAMA                                                                       |
===================================================================================================================================================='''
if __name__ == "__main__":
    thread_jam = threading.Thread(target=pengelolaan.simulasi_jam, daemon=True)
    thread_jam.start()
    thread_dapur = threading.Thread(target=dapur_.masak, daemon=True)
    thread_dapur.start()
    shared.log_queue.put(f"[Dapur] Istirahat...")
    try:
        while True:
            if pengelolaan.jam_operasional():   
                tampilkan_menu_utama()
            else:
                reservasi.bersihkan_pengunjung()
                pemesanan.bersihkan_pesanan()
                tampilkan_layar_terkunci()
    except KeyboardInterrupt:
        waktu_program["berjalan"] = False
        print("\nProgram dihentikan.")