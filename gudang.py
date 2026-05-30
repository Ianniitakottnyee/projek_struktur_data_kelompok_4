import pengelolaan
import shared


'''
MINGGU 4
====================================================================================================================================================
|                                                                       GUDANG                                                                       |
===================================================================================================================================================='''
class Gudang:
    def __init__(self):
        self.kapasitas_maks = 2100
        data = pengelolaan.akses()
        self.stok = data[1]

    def total_stok(self):
        total = 0
        for jumlah in self.stok.values():
            total += jumlah
        return total

    def sisa_kapasitas(self):
        return self.kapasitas_maks - self.total_stok()

    def beli_bahan(self, nama_bahan, jumlah):
        if self.total_stok() + jumlah > self.kapasitas_maks:
            print("[GUDANG] Kapasitas tidak cukup!")
            return
        if nama_bahan not in self.stok:
            self.stok[nama_bahan] = 0
        self.stok[nama_bahan] = round(self.stok[nama_bahan] + jumlah, 1)
        shared.log_queue.put("\033[92m" + f"[GUDANG] Berhasil membeli {jumlah} {nama_bahan}" + "\033[0m")

    def gunakan_bahan(self, nama_bahan, jumlah):
        if nama_bahan not in self.stok:
            shared.log_queue.put("[ERROR] Bahan tidak ditemukan.")
            return
        if self.stok[nama_bahan] < jumlah:
            shared.log_queue.put(f"[ERROR] Stok {nama_bahan} tidak cukup.")
            self.beli_bahan(nama_bahan,jumlah+5)
            return
        self.stok[nama_bahan] = round(self.stok[nama_bahan] - jumlah, 1)
        shared.log_queue.put("\033[92m" + f"[DAPUR] Menggunakan {jumlah} {nama_bahan}" + "\033[0m")
        pengelolaan.Simpan(stok=self.stok)

    def tampilkan_stok(self):
        print("\n=== STOK GUDANG ===")
        for bahan, jumlah in self.stok.items():
            print(f"{bahan}: {jumlah}")
        print(f"\nTotal Isi Gudang : {self.total_stok():.1f}")
        print(f"Sisa Kapasitas   : {self.sisa_kapasitas():.1f}")

