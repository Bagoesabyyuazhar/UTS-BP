def jualan():
    minuman1 = "capucino"
    minuman2 = "teh"
    print("Pilihan")
    print("1.", minuman1)
    print("2.", minuman2)
    print("3. Exit")


def Capucino():
    cap = "memilih CAPUCINO"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = capucino * 10/100
    total = print("Terkena ppn sebesar 10% :", capucino + ppn)
    print(total)


def Teh():
    teh = "memilih TEH"
    print(teh)
    teh = int(input("masukkan harga : "))
    ppn = teh * 10/100
    total = print("Terkena ppn sebesar 10% :", teh + ppn)
    print(total)


def welcome():
    nim = 20210801253
    nama = "Bagoes"
    print("NIM : ", nim)
    print("NAMA : ", nama)


while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        Capucino()
    elif pil == 2:
        Teh()
    elif pil == 3:
        break
    else:
        print("pilihan salah")