import pengelolaan


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
    data = pengelolaan.akses()
    delivery.graph = data[5]
    dari = input("dari: ").title()
    ke = input("ke: ").title()
    jarak = pengelolaan.Cek("jarak: ", "jarak tidak valid!")
    delivery.tambah_jalan(dari, ke, jarak)
    pengelolaan.Simpan(peta= delivery.graph)
    print("Berhasil menambahkan lokasi baru.")

''' TAMPILKAN PETA '''
def peta():
    data = pengelolaan.akses()
    delivery.graph = data[5]
    delivery.tampilkan()

''' ANTAR PESANAN '''
def pengantaran():
    data = pengelolaan.akses()
    delivery.graph = data[5]
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