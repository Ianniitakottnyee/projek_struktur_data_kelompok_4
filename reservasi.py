import pengelolaan


'''
MINGGU 2
====================================================================================================================================================
|                                                                       RESERVASI                                                                       |
===================================================================================================================================================='''
''' RESERVASI PELANGGAN '''
def reservasi_():
    ambil = pengelolaan.akses()
    antrian = ambil[2]
    try:
        if antrian == []:
            no = 1
        else:
            no = antrian[-1]["antrian"] + 1
    except (KeyError, IndexError):
        no = 1
    nama = input("Reservasi atas nama: ")
    data = {"nama": nama.title(), "antrian": no}
    antrian.append(data)
    pengelolaan.Simpan(antrian= antrian)
    return nama

''' TAMPILKAN PENGUNJUNG HARI INI '''
def tampilkan_pengunjung():
    data = pengelolaan.akses()
    antrian = data[2]
    print("Pengunjung hari ini: ")
    no = 1
    for x in antrian:
        print(f"[Antrian {no}] {x['nama']}")
        no += 1

''' BERSIHKAN PENGUNJUNG '''
def bersihkan_pengunjung():
    pengelolaan.Simpan(antrian= [])