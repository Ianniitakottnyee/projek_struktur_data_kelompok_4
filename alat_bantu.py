def Cek(pesan, eror):
    while True:    
        try:
            x = int(input(pesan))
            break
        except ValueError: print(eror)
    return x