import pengelolaan
import time
import shared

dapur = None

def set_dapur(queue):
    global dapur
    dapur = queue

'''
MINGGU 3
====================================================================================================================================================
|                                                                       DAPUR                                                                       |
===================================================================================================================================================='''



''' CLASS NODE DAPUR '''
class OrderNode:
    def __init__(self, nomor, nama, daftar_menu):
        self.nomor = nomor
        self.nama = nama
        self.daftar_menu = daftar_menu
        self.next = None

''' CLASS ANTRIAN DAPUR QUEUE'''
class KitchenQueue:
    def __init__(self):
        self.head = None

    ''' TAMBAH ANTRIAN '''
    def tambah_pesanan(self, nama, daftar_menu):
        shared.nomor_pesanan += 1
        new_order = OrderNode(shared.nomor_pesanan, nama, daftar_menu)
        if self.head is None:
            self.head = new_order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order
        print(f"[DAPUR] Pesanan {nama} masuk antrean.")

    ''' TAMBAH ANTRIAN PRIORITAS '''
    def tambah_prioritas(self, nama, daftar_menu):
        shared.nomor_pesanan += 1
        new_order = OrderNode(shared.nomor_pesanan, nama, daftar_menu)
        new_order.next = self.head
        self.head = new_order
        print(f"[PRIORITAS] Pesanan VIP {nama} diprioritaskan.")

    ''' TAMPILKAN ANTRIAN DAPUR '''
    def tampilkan_antrean(self):
        if self.head is None and shared.diproses is None:
            print("Tidak ada antrean.")
            return
        current = self.head
        print("\n=== ANTREAN DAPUR ===")
        if shared.diproses is not None:
            print(f"\nNo Pesanan : {shared.diproses.nomor}")
            print(f"Pelanggan  : {shared.diproses.nama}")
            print("Menu:")
            for menu in shared.diproses.daftar_menu:
                print(f"- {menu}")
            print(" [STATUS] Sedang diproses...")
        while current:
            print(f"\nNo Pesanan : {current.nomor}")
            print(f"Pelanggan  : {current.nama}")
            print("Menu:")
            for menu in current.daftar_menu:
                print(f"- {menu}")
            print(" [STATUS] Dalam antrian...")
            current = current.next

    def proses(self):
        if self.head is None:
            return
        shared.diproses = self.head
        self.head = self.head.next
        return [shared.diproses.nomor, shared.diproses.nama, shared.diproses.daftar_menu]


''' MASAK '''
def masak_pesanan(pesanan):
    data = pengelolaan.akses()
    kumpulan_resep = data[4]
    resep = None
    total_bahan = {}
    for menu in pesanan:
        if menu in kumpulan_resep.keys():
            resep = kumpulan_resep[f"{menu}"]
            for bahan, jumlah in resep.items():
                if bahan not in total_bahan:
                    total_bahan[bahan] = 0
                total_bahan[bahan] += jumlah
    for bahan, jumlah in total_bahan.items():
        shared.penyimpanan.gunakan_bahan(nama_bahan=bahan, jumlah=jumlah)
    
def masak():
    while True:
        if dapur is None:
            time.sleep(1)
            continue
        ket = dapur.proses()
        if ket is not None:
            masak_pesanan(ket[2])
            time.sleep(10 * len(ket[2]))
            shared.log_queue.put("\033[91m" + f"[Dapur] Pesanan #{ket[0]} atas nama {ket[1]} selesai dimasak" + "\033[0m")
            shared.diproses = None
        else:
            time.sleep(10)

