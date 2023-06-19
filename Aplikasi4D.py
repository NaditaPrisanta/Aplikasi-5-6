# Hitung Luas atau Volume Balok

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS ATAU VOLUME BALOK")
print("--------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Luas atau Volume (Luas/Volume): ")

    if pilihan.upper() == "LUAS":
        Panjang = int(input("Masukkan Panjang Balok: "))
        Lebar = int(input("Masukkan Lebar Balok: "))
        Tinggi = int(input("Masukkan Tinggi Balok: "))

        Luas_Permukaan = 2 * (Panjang *Lebar + Panjang * Tinggi + Lebar * Tinggi)
        print("Luas Permukaan Balok: ", Luas_Permukaan)
    elif pilihan.upper() == "VOLUME":
        Panjang = int(input("Masukkan Panjang Balok: "))
        Lebar = int(input("Masukkan Lebar Balok: "))
        Tinggi = int(input("Masukkan Tinggi Balok: "))

        Volume = Panjang * Lebar * Tinggi
        print("Volume Balok: ", Volume)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    