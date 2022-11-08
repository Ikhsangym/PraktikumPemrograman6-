def Biodata(tahunLahir, Namaku, Asal):
    tahunsekarang = 2020
    print(f"perkenalkan Nama Saya : {Namaku}")      
    print(f"Umur Saya : {tahunsekarang - tahunLahir} ")
    print(f"Asal Saya dari : {Asal}")
tahunLahir = int(input())
Namaku = input()
Asal = input()
Biodata(tahunLahir, Namaku, Asal)