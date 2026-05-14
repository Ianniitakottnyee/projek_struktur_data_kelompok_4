import alat_bantu

class DeliveryGraph:
    def __init__(self):
        self.graph = {}

    # Tambah lokasi/jalan
    def tambah_jalan(self, dari, ke, jarak):

        # Jika node belum ada
        if dari not in self.graph:
            self.graph[dari] = {}

        if ke not in self.graph:
            self.graph[ke] = {}

        # Dua arah
        self.graph[dari][ke] = jarak
        self.graph[ke][dari] = jarak

    # Tampilkan graph
    def tampilkan(self):
        print("\n=== PETA DELIVERY ===")

        for lokasi in self.graph:
            print(f"{lokasi} -> {self.graph[lokasi]}")

    # DFS sederhana
    def cari_rute(self, awal, tujuan, visited=None):

        if visited is None:
            visited = []

        visited.append(awal)

        if awal == tujuan:
            return visited

        for tetangga in self.graph[awal]:

            if tetangga not in visited:

                hasil = self.cari_rute(
                    tetangga,
                    tujuan,
                    visited.copy()
                )

                if hasil:
                    return hasil
        return None
delivery = DeliveryGraph()
def tambah_jalan():
    dari = input("dari: ")
    ke = input("ke: ")
    jarak = alat_bantu.Cek("jarak: ", "jarak tidak valid!")
    delivery.tambah_jalan(dari, ke, jarak)

def peta():
    delivery.tampilkan()

def pengantaran():
    dari = "Resto"
    ke = input("antar pesanan ke ")
    rute = delivery.cari_rute(dari, ke)
    print("Rute pengiriman: ")
    print(" -> ".join(rute))