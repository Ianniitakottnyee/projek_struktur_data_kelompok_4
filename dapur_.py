nomor_pesanan = 0

# =========================================
# NODE PESANAN
# =========================================
class OrderNode:
    def __init__(self, nomor, pelanggan, daftar_menu):

        self.nomor = nomor
        self.pelanggan = pelanggan
        self.daftar_menu = daftar_menu

        self.next = None


# =========================================
# LINKED LIST DAPUR
# =========================================
class KitchenQueue:
    def __init__(self):
        self.head = None

    # =====================================
    # TAMBAHKAN PESANAN
    # =====================================
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

    # =====================================
    # TAMBAHKAN PRIORITAS
    # =====================================
    def tambah_prioritas(self, nomor, pelanggan, daftar_menu):
        new_order = OrderNode(nomor, pelanggan, daftar_menu)
        new_order.next = self.head
        self.head = new_order
        print(f"[PRIORITAS] Pesanan VIP {pelanggan} diprioritaskan.")

    # =====================================
    # SELESAIKAN PESANAN
    # =====================================
    def selesai_pesanan(self):
        if self.head is None:
            print("Antrean dapur kosong.")
            return
        selesai = self.head
        self.head = self.head.next
        print(f"[SELESAI] Pesanan {selesai.pelanggan} selesai dimasak.")

    # =====================================
    # TAMPILKAN ANTREAN
    # =====================================
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
    # =====================================
    # PROSES PESANAN
    # =====================================
    def proses(self):
        if self.head is None:
            print("Tidak ada antrean.")
        current = self.head
        for menu in current.daftar_menu:
            ...



# =========================================
# FUNGSI UNTUK ANTRIAN DAPUR
# =========================================
dapur = KitchenQueue()
def antrian_dapur(nama, pesanan):
    global nomor_pesanan
    nomor_pesanan += 1

    dapur.tambah_pesanan(nomor_pesanan, nama, pesanan)

def tampilkan_dapur():
    dapur.tampilkan_antrean()

def prioritas(nama, pesanan):
    global nomor_pesanan
    nomor_pesanan += 1

    dapur.tambah_prioritas(nomor_pesanan, nama, pesanan)

def masak():
    ...