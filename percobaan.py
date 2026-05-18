import threading
import time
import os
import json

'''
====================================================================================================================================================
|                                                                PENGELOLAAN                                                                       |
===================================================================================================================================================='''
''' CEK INPUT HARUS BERBENTUK INTEGER '''
def Cek(pesan, eror):
    while True:    
        try:
            x = int(input(pesan))
            break
        except ValueError: print(eror)
    return x

''' SIMPAN DATA KE .JSON '''
def Save(simpan):
    with open("data_resto.json", "w") as f:
        json.dump(simpan, f)

''' BUKA DATA DARI .JSON '''
def Open():
    with open("data_resto.json", "r") as f:
        loaded = json.load(f)
    return loaded

''' AMBIL DATA DARI .JSON '''
def akses():
    data = Open()
    try:
        menu = data["Menu"]
    except KeyError: menu = []
    try:
        stok_bahan = data["stok_bahan"]
    except KeyError: stok_bahan = []     
    try:
        antrian = data["antrian"]      
    except KeyError: antrian = []
    try:
        pesanan = data["pesanan"]
    except KeyError: pesanan = []
    return [menu, stok_bahan, antrian, pesanan]

''' VARIABEL GLOBAL WAKTU '''
waktu_program = {
    "hari": 1,
    "jam": 6, 
    "menit": 30,
    "detik": 0,
    "berjalan": True
}

''' RESET WAKTU '''
def reset():
    global waktu_program
    if waktu_program["jam"] % 24 > 21:
        waktu_program["jam"] = waktu_program["jam"] + (31 - (waktu_program["jam"] % 24))
        waktu_program["menit"] = 0
    elif waktu_program["jam"] % 24 < 7:
        waktu_program["jam"] = waktu_program["jam"] + (7 - (waktu_program["jam"] % 24))
        waktu_program["menit"] = 0
    else:
        waktu_program["jam"] = waktu_program["jam"] + (22 - (waktu_program["jam"] % 24))
        waktu_program["menit"] = 0
        
''' JAM LOKAL '''
def simulasi_jam():
    global waktu_program
    perdetik = 72
    sisa_detik = 0
    while waktu_program["berjalan"]:
        total_detik_baru = waktu_program["menit"] * 60 + sisa_detik + perdetik
        menit_tambahan = total_detik_baru // 60
        sisa_detik = total_detik_baru % 60
        waktu_program["menit"] = menit_tambahan % 60
        
        total_jam_baru = waktu_program["jam"] + menit_tambahan // 60
        waktu_program["jam"] = total_jam_baru % 24
        waktu_program["hari"] = 1 + (total_jam_baru // 24)
        time.sleep(1)

''' JAM OPERASIONAL CAFE '''
def jam_operasional():
    jam_sekarang = waktu_program["jam"]
    if 7 <= jam_sekarang < 22:
        return True
    return False

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
    ambil = akses()
    q = ambil[2]
    print("[1] Reservasi Pelanggan")
    print("[2] Lihat Menu")
    print("[3] Daftar Antrian")
    print("[4] Pesan antar")
    print("[5] Peta")
    print("[6] Antrian Dapur")

    print("====================================")
    if log_queue.empty():
        log_queue.put(f"[Dapur] Istirahat...")
    mulai()
    print("====================================\n")

    mode = Cek("Pilih: ", "Input harus berupa angka!")
    if mode == 0:
        ...
    
    elif mode == 1:
        siapa = reservasi_()
        pesanan(siapa)
        input("\nTekan enter untuk keluar...")

    elif mode == 2:
        x = akses()
        root = build_tree("Menu", x[0])

        print("=========== DAFTAR MENU ===========")
        tampilkan_tree(root)
        input("\nTekan enter untuk keluar...")

    elif mode == 3:
        tampilkan_antrian()
        input("\nTekan enter untuk keluar...")

    elif mode == 4:
        ...
        pengantaran()
        input("\nTekan enter untuk keluar...")

    elif mode == 5:
        print(" [1] Tambahkan lokasi baru.")
        print(" [2] Lihat peta")
        pilih = Cek("Pilihan: ", "Input tidak valid.")
        if pilih == 1:
            tambah_jalan()
        elif pilih == 2:
            peta()
        input("\nTekan enter untuk keluar...")

    elif mode == 6:
        tampilkan_dapur()
        input("\nTekan enter untuk keluar...")

    elif mode == -1:
        reset()

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
        reset()

'''
MINGGU 1
====================================================================================================================================================
|                                                                        MENU                                                                       |
===================================================================================================================================================='''
''' CLASS NODE MENU '''
class TreeNode:
    def __init__(self, nama, data=None):
        self.nama = nama
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

''' TREE '''
def build_tree(nama, struktur):
    node = TreeNode(nama)
    if isinstance(struktur, dict):
        for key, value in struktur.items():
            child = build_tree(key, value)
            node.add_child(child)
    elif isinstance(struktur, list):
        for item in struktur:
            item_node = TreeNode(item["nama"], data=item)
            node.add_child(item_node)
    return node

''' TAMPILKAN MENU '''
def tampilkan_tree(node, level=0):
    indent = "    " * level
    if node.data:
        print(f"{indent}[{node.data['kode']}] {node.data['nama'].ljust(20)} Rp.{node.data['harga']}")
    else:
        print(f"{indent}{node.nama}")
    for child in node.children:
        tampilkan_tree(child, level + 1)

''' CARI MENU '''
def cari_menu(node, kode):
    if node.data and node.data["kode"] == kode:
        return node.data
    for child in node.children:
        hasil = cari_menu(child, kode)
        if hasil:
            return hasil
    return None

''' INDEX '''
index_menu = {}
def index_tree(node):
    if node.data:
        index_menu[node.data["kode"]] = node.data
    for child in node.children:
        index_tree(child)

'''
MINGGU 2
====================================================================================================================================================
|                                                                       RESERVASI                                                                       |
===================================================================================================================================================='''
''' RESERVASI PELANGGAN '''
def reservasi_():
    ambil = akses()
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
    Save(simpan)
    return nama

''' TAMPILKAN ANTRIAN '''
def tampilkan_antrian():
    data = akses()
    antrian = data[2]
    print("Antrian saat ini: ")
    no = 1
    for x in antrian:
        print(f"[Antrian {no}] {x["nama"]}")
        no += 1

''' BERSIHKAN ANTRIAN '''
def bersihkan_antrian():
    ambil = akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [], "pesanan": ambil[3]}
    Save(simpan)


'''
MINGGU 2
====================================================================================================================================================
|                                                                       PEMESANAN                                                                       |
===================================================================================================================================================='''
''' PEMESANAN '''
def pesanan(siapa):
    ambil = akses()
    kumpulan_pesanan = ambil[3]
    vip = input("Pesanan prioritas(ya/tidak): ")

    x = akses()
    root = build_tree("Menu", x[0])
    print("=== DAFTAR MENU ===")
    tampilkan_tree(root)
    index_tree(root)

    print("\n=== Pilih Pesanan ===")
    semua_pesanan = []
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
            print(f"Ditemukan: {hasil["nama"].ljust(15)} Rp.{hasil["harga"]}")
            semua_pesanan.append(hasil["nama"])
        else:
            print("Menu tidak ditemukan")
    pesanan_siapa = {"nama": siapa, "pesanan": semua_pesanan}
    kumpulan_pesanan.append(pesanan_siapa)
    if vip == "ya":
        prioritas(nama= siapa, pesanan= semua_pesanan)
    else:
        antrian_dapur(nama= siapa, pesanan= semua_pesanan)

    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": ambil[2], "pesanan": kumpulan_pesanan}
    Save(simpan)

''' BERSIHKAN PESANAN '''
def bersihkan_pesanan():
    ambil = akses()
    simpan = {"Menu": ambil[0], "stok_bahan": ambil[1], "antrian": [2], "pesanan": []}
    Save(simpan)


'''
MINGGU 3
====================================================================================================================================================
|                                                                       DAPUR                                                                       |
===================================================================================================================================================='''
from queue import Queue
log_queue = Queue()
nomor_pesanan = 0
hari = 1

''' CLASS NODE DAPUR '''
class OrderNode:
    def __init__(self, nomor, pelanggan, daftar_menu):

        self.nomor = nomor
        self.pelanggan = pelanggan
        self.daftar_menu = daftar_menu

        self.next = None

''' CLASS ANTRIAN DAPUR QUEUE'''
class KitchenQueue:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, nomor, pelanggan, daftar_menu):
        new_order = OrderNode(nomor, pelanggan, daftar_menu)
        if self.head is None:
            self.head = new_order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order
        print(f"[DAPUR] Pesanan {pelanggan} masuk antrean.")

    def tambah_prioritas(self, nomor, pelanggan, daftar_menu):
        new_order = OrderNode(nomor, pelanggan, daftar_menu)
        new_order.next = self.head
        self.head = new_order
        print(f"[PRIORITAS] Pesanan VIP {pelanggan} diprioritaskan.")

    def tampilkan_antrean(self):
        if self.head is None:
            print("Tidak ada antrean.")
            return
        current = self.head
        print("\n=== ANTREAN DAPUR ===")
        while current:
            print(f"\nNo Pesanan : {current.nomor}")
            print(f"Pelanggan  : {current.pelanggan}")
            print("Menu:")
            for menu in current.daftar_menu:
                print(f"- {menu}")
            current = current.next

    def proses(self):
        if self.head is None:
            return
        masak = self.head
        self.head = self.head.next
        return [masak.nomor, masak.pelanggan, masak.daftar_menu]

dapur = KitchenQueue()
''' TAMBAH ANTRIAN '''
def antrian_dapur(nama, pesanan):
    global nomor_pesanan
    nomor_pesanan += 1
    dapur.tambah_pesanan(nomor_pesanan, nama, pesanan)

''' TAMBAH ANTRIAN PRIORITAS '''
def prioritas(nama, pesanan):
    global nomor_pesanan
    nomor_pesanan += 1
    dapur.tambah_prioritas(nomor_pesanan, nama, pesanan)

''' TAMPILKAN ANTRIAN DAPUR '''
def tampilkan_dapur():
    dapur.tampilkan_antrean()

''' MASAK '''
def masak():
    data = akses()
    antrian = data[2]
    while True:
        ket = dapur.proses()
        if ket is not None:
            log_queue.put(f"[Dapur] Pesanan #{ket[0]} atas nama {ket[1]} sedang diproses")
            time.sleep(4 * len(ket[2]))
            log_queue.put(f"[Dapur] Pesanan #{ket[0]} atas nama {ket[1]} selesai dimasak")
            for i, x in enumerate(antrian):
                if x["nama"] == ket[1]:
                    antrian.pop(i)
                    break
            simpan = {"Menu": data[0], "stok_bahan": data[1], "antrian": antrian, "pesanan": data[3]}            
            Save(simpan)
        else:
            time.sleep(1)


''' PRINT ANTRIAN PESAN '''
def mulai():
    while not log_queue.empty():
        pesan = log_queue.get()
        print(pesan)
        log_queue.task_done()

        
'''
MINGGU 3
====================================================================================================================================================
|                                                                   DELIVERI                                                                       |
===================================================================================================================================================='''
''' CLASS DELIVERI GRAPH '''
import heapq

class DeliveryGraph:
    def __init__(self):
        self.graph = {}

    def tambah_jalan(self, dari, ke, jarak):
        if dari not in self.graph:
            self.graph[dari] = {}
        if ke not in self.graph:
            self.graph[ke] = {}
        self.graph[dari][ke] = jarak
        self.graph[ke][dari] = jarak

    def tampilkan(self):
        print("\n=== PETA DELIVERY ===")
        for lokasi in self.graph:
            print(f"{lokasi} -> {self.graph[lokasi]}")

    def cari_rute(self, awal, tujuan):
        pq = []
        heapq.heappush(pq, (0, awal, [awal]))
        visited = set()
        while pq:
            total_jarak, lokasi, jalur = heapq.heappop(pq)
            if lokasi in visited:
                continue
            visited.add(lokasi)
            if lokasi == tujuan:
                return jalur, total_jarak
            for tetangga in self.graph[lokasi]:
                if tetangga not in visited:
                    jarak = self.graph[lokasi][tetangga]
                    heapq.heappush(pq,(total_jarak + jarak, tetangga, jalur + [tetangga]))
        return None, None

''' TAMBAH LOKASI '''
delivery = DeliveryGraph()
def tambah_jalan():
    dari = input("dari: ")
    ke = input("ke: ")
    jarak = Cek("jarak: ", "jarak tidak valid!")
    delivery.tambah_jalan(dari.title(), ke.title(), jarak)

''' TAMPILKAN PETA '''
def peta():
    delivery.tampilkan()

''' ANTAR PESANAN '''
def pengantaran():
    dari = "Resto"
    ke = input("antar pesanan ke ").title()
    rute, jarak = delivery.cari_rute(dari, ke)
    if rute is None:
        print("Lokasi tidak ditemukan")
        return

    print("============= Deliveri =============")
    print(f"Tujuan: {ke}")
    print(f"Rute: {" -> ".join(rute)}")
    print(f"Jarak: {jarak} km")
    
'''
====================================================================================================================================================
|                                                                   PROGRAM UTAMA                                                                       |
===================================================================================================================================================='''
if __name__ == "__main__":
    thread_jam = threading.Thread(target=simulasi_jam, daemon=True)
    thread_jam.start()
    thread_dapur = threading.Thread(target=masak, daemon=True)
    thread_dapur.start()
    log_queue.put(f"[Dapur] Istirahat...")
    try:
        while True:
            if jam_operasional():   
                tampilkan_menu_utama()
            else:
                bersihkan_antrian()
                tampilkan_layar_terkunci()
    except KeyboardInterrupt:
        waktu_program["berjalan"] = False
        print("\nProgram dihentikan.")


'''
jarak di deliveri
rapikan menu
deliveri asal "Resto" .titlekan
json, menu & stok bahan baru
'''