import time
import threading
hari = 1
tutup = False

def operasional():
    global tutup
    global hari
    while tutup == False:
        print(f"[Hari ke-{hari}] Buka!")
        print("[Jam] 07:00")
        time.sleep(5)
        print("[Jam] 12:00")
        time.sleep(5)
        print("[Jam] 17:00")
        time.sleep(5)
        print("[Jam] 22:00")
        print("Tutup!")
        tutup = True
    time.sleep(9)
    hari += 1
    tutup = False
    operasional()


t = threading.Thread(target=operasional)
t.start()
x = input("pesan apa yh: ")
print(f"pesanan kmu: {x}")