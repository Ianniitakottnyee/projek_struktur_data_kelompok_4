import pengelolaan
import menu
import shared
from menu import tampilkan_tree, index_tree, index_menu


'''
MINGGU 2
====================================================================================================================================================
|                                                                       PEMESANAN                                                                       |
===================================================================================================================================================='''
''' PEMESANAN '''
def pesanan(siapa):
    ambil = pengelolaan.akses()
    kumpulan_pesanan = ambil[3]
    vip = input("Pesanan prioritas(ya/tidak): ")

    root = menu.build_tree("Menu", ambil[0])
    print("=== DAFTAR MENU ===")
    tampilkan_tree(root)
    index_tree(root)

    print("\n=== Pilih Pesanan ===")
    semua_pesanan = []
    print("Pilih menu berdasarkan kode(ketik '.' untuk selesai memesan dan '/batal' untuk membatalkan pesanan).")
    while True:
        kode_dicari = input("kode  ")
        if kode_dicari == ".":
            break
        if kode_dicari == "/batal" or kode_dicari == "/undo":
            if semua_pesanan == []:
                print("belum ada pesanan yang tercatat" )
            else:
                batal = semua_pesanan.pop()
                print(f"{batal} berhasil dibatalkan dari pesanan.")
                continue
        else:
            kode_dicari = kode_dicari.title()
        hasil = index_menu.get(kode_dicari)
        if hasil:
            print(f"Ditemukan: {hasil['nama'].ljust(15)} Rp.{hasil['harga']}")
            semua_pesanan.append(hasil['nama'])
        else:
            print("Menu tidak ditemukan")
    pesanan_siapa = {"nama": siapa, "pesanan": semua_pesanan}
    kumpulan_pesanan.append(pesanan_siapa)
    if vip == "ya":
        shared.memasak.tambah_prioritas(nama= siapa, daftar_menu= semua_pesanan)
    else:
        shared.memasak.tambah_pesanan(nama= siapa, daftar_menu= semua_pesanan)

    pengelolaan.Simpan(pesanan= kumpulan_pesanan)

''' BERSIHKAN PESANAN '''
def bersihkan_pesanan():
    pengelolaan.Simpan(pesanan= [])