# Hitung Luas dan Volume Balok

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS DAN VOLUME BALOK")
print("--------------------------------------------------------------------------------")

while True:
    Panjang = int(input("Masukkan Panjang Balok: "))
    Lebar = int(input("Masukkan Lebar Balok: "))
    Tinggi = int(input("Masukkan Tinggi Balok: "))

    Luas_Permukaan = 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)
    Volume = Panjang * Lebar * Tinggi

    print("Luas Permukaan Balok: ", Luas_Permukaan)
    print("Volume Balok: ", Volume)

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Apakah Anda ingin menghitung lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break
