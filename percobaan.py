import threading
import time
import os
import reservasi
import pengelolaan
import menu
import deliveri
import dapur_
import pemesanan

# Struktur data global untuk menyimpan status waktu dan menu
game_time = {
    "hari": 1,
    "jam": 6,       # Mulai dari jam 6 pagi agar bisa melihat transisi ke jam 7
    "menit": 30,
    "detik": 0,
    "berjalan": True
}

def reset():
    global game_time
    if game_time["jam"] % 24 > 21:
        game_time["jam"] = game_time["jam"] + (31 - (game_time["jam"] % 24))
        game_time["menit"] = 0
    elif game_time["jam"] % 24 < 7:
        game_time["jam"] = game_time["jam"] + (7 - (game_time["jam"] % 24))
        game_time["menit"] = 0
    else:
        game_time["jam"] = game_time["jam"] + (22 - (game_time["jam"] % 24))
        game_time["menit"] = 0
        

# 1 jam game = 50 detik nyata
# 1 detik nyata = 72 detik game (1 menit 12 detik game)

def simulasi_jam():
    """Fungsi latar belakang (thread) untuk menjalankan jam."""
    global game_time
    perdetik = 72
    sisa_detik = 0
    while game_time["berjalan"]:
        # Update menit di dalam game setiap 1 detik nyata
        total_detik_baru = game_time["menit"] * 60 + sisa_detik + perdetik#72
        menit_tambahan = total_detik_baru // 60 #1
        sisa_detik = total_detik_baru % 60 #12
        game_time["menit"] = menit_tambahan % 60
        
        # Update jam
        total_jam_baru = game_time["jam"] + menit_tambahan // 60
        game_time["jam"] = total_jam_baru % 24
        game_time["hari"] = 1 + (total_jam_baru // 24)
        time.sleep(1)

def cek_jam_operasional():
    """Memeriksa apakah jam saat ini berada antara pukul 07:00 hingga 22:00."""
    jam_sekarang = game_time["jam"]
    # Operasional: 7 pagi (07:00) sampai 10 malam (22:00)
    if 7 <= jam_sekarang < 22:
        return True
    return False

def tampilkan_menu_utama():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================")
    print("============ Cs.in Cafe ============")
    print("====================================") 
    print(f"Jam Sekarang: {game_time['jam']:02d}:{game_time['menit']:02d}")
    print("------------------------------------")
    print("Status: BUKA")
    print("Selamat datang di Cs.in Cafe🍜")
    print("====================================")
    ambil = pengelolaan.akses()
    q = ambil[2]
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
    if mode == 0:
        reset()
    
    elif mode == 1:
        reservasi.reservasi_()

    elif mode == 2:
        x = pengelolaan.akses()
        root = menu.build_tree("Menu", x[0])

        print("=== DAFTAR MENU ===")
        menu.tampilkan_tree(root)
        keluar = input("\nTekan enter untuk keluar menu...")

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



def tampilkan_layar_terkunci():
    global game_time
    game_time["jam"] = game_time["jam"] % 24
    """Layar kunci ketika di luar jam operasional."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================")
    print("      Toko / Layanan Sedang Tutup   ")
    print("====================================")
    print(f"Jam Sekarang: {game_time['jam']:02d}:{game_time['menit']:02d}")
    print("------------------------------------")
    print("Status: MENU UTAMA TIDAK DAPAT DIAKSES")
    print("Jam Operasional: 07:00 s/d 22:00")
    print("====================================")
    print("Tekan ENTER untuk cek waktu atau 'exit' untuk keluar.")
    print("Ketik /skip untuk tidur.")
    pilihan = input(">> ").lower()
    if pilihan == "exit":
        game_time["berjalan"] = False
        exit()
    elif pilihan == "/skip":
        reset()

# --- Program Utama ---
if __name__ == "__main__":
    thread_jam = threading.Thread(target=simulasi_jam, daemon=True)
    thread_jam.start()
    
    try:
        while True:
            if cek_jam_operasional():
                tampilkan_menu_utama()
            else:
                tampilkan_layar_terkunci()
    except KeyboardInterrupt:
        game_time["berjalan"] = False
        print("\nProgram dihentikan.")