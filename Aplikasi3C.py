#Hitung Luas dan Keliling Segitiga

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS DAN KELILING SEGITIGA")
print("--------------------------------------------------------------------------------")

import math

while True:
    Alas = int(input("Masukkan Panjang Alas Segitiga: "))
    Tinggi = int(input("Masukkan Tinggi Segitiga: "))
    Sisi1 = int(input("Masukkan Panjang Sisi1: "))
    Sisi2 = int(input("Masukkan Panjang Sisi2: "))
    Sisi3 = int(input("Masukkan Panjang Sisi3: "))

    Luas = 0.5 * Alas * Tinggi
    Keliling = Sisi1 + Sisi2 + Sisi3

    print("Luas Segitiga: ", Luas)
    print("Keliling Segitiga: ", Keliling)

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break