import json
import time
import shared


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
        json.dump(simpan, f, indent=4)

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
    try:
        resep = data["resep"]
    except KeyError: resep = {}
    try:
        peta = data["peta"]
    except KeyError: peta = {}

    return [menu, stok_bahan, antrian, pesanan, resep, peta]

''' SIMPAN DATA '''
def Simpan(menu=None, stok=None, antrian=None, pesanan=None, resep=None, peta=None):
    data = akses()
    try:
        if menu is None:
            menu = data[0]
        if stok is None:
            stok = data[1]
        if antrian is None:
            antrian = data[2]
        if pesanan is None:
            pesanan = data[3]
        if resep is None:
            resep = data[4]
        if peta is None:
            peta = data[5]
    except KeyError:
        ...
    simpan = {"Menu": menu, "stok_bahan": stok, "antrian": antrian, "pesanan": pesanan, "resep": resep, "peta": peta}
    Save(simpan)

''' VARIABEL GLOBAL WAKTU '''


''' RESET WAKTU '''
def reset():
    if shared.waktu_program["jam"] % 24 > 21:
        shared.waktu_program["jam"] = shared.waktu_program["jam"] + (31 - (shared.waktu_program["jam"] % 24))
        shared.waktu_program["menit"] = 0
    elif shared.waktu_program["jam"] % 24 < 7:
        shared.waktu_program["jam"] = shared.waktu_program["jam"] + (7 - (shared.waktu_program["jam"] % 24))
        shared.waktu_program["menit"] = 0
    else:
        shared.waktu_program["jam"] = shared.waktu_program["jam"] + (22 - (shared.waktu_program["jam"] % 24))
        shared.waktu_program["menit"] = 0
        
''' JAM LOKAL '''
def simulasi_jam():
    perdetik = 72
    sisa_detik = 0
    while shared.waktu_program["berjalan"]:
        total_detik_baru = shared.waktu_program["menit"] * 60 + sisa_detik + perdetik
        menit_tambahan = total_detik_baru // 60
        sisa_detik = total_detik_baru % 60
        shared.waktu_program["menit"] = menit_tambahan % 60
        
        total_jam_baru = shared.waktu_program["jam"] + menit_tambahan // 60
        shared.waktu_program["jam"] = total_jam_baru % 24
        shared.waktu_program["hari"] = 1 + (total_jam_baru // 24)
        time.sleep(1)

''' JAM OPERASIONAL CAFE '''
def jam_operasional():
    jam_sekarang = shared.waktu_program["jam"]
    if 7 <= jam_sekarang < 22:
        return True
    return False

''' PRINT ANTRIAN PESAN '''
def mulai():
    while not shared.log_queue.empty():
        pesan = shared.log_queue.get()
        print(pesan)
        shared.log_queue.task_done()

