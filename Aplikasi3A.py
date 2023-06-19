# Hitung Luas dan Keliling Persegi Panjang

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS DAN KELILING PERSEGI PANJANG")
print("--------------------------------------------------------------------------------")

while True:
    Panjang = int(input("Masukkan Panjang Persegi Panjang: "))
    Lebar = int(input("Masukkan Lebar Persegi Panjang: "))

    Luas = Panjang * Lebar
    Keliling = 2 * (Panjang + Lebar)

    print("Luas Persegi Panjang: ", Luas)
    print("Keliling Persegi Panjang: ", Keliling)
    
    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Ingin Menghitung lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break