def Biodata(tahunLahir, Namaku, Asal):
    tahunsekarang = 2020
    print("perkenalkan Nama Saya : {} ".format(Namaku))      
    print("Umur Saya : {} ".format(tahunsekarang - tahunLahir))
    print("Asal Saya dari : {} ".format(Asal))
tahunLahir = int(input())
Namaku = input()
Asal = input()
Biodata(tahunLahir, Namaku, Asal)