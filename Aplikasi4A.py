# Hitung Luas atau Keliling persegi panjang 

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS ATAU KELILING DARI PERSEGI PANJANG")
print("--------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Luas atau Keliling (Luas/Keliling): ")

    if pilihan.upper() == "LUAS":
        Panjang = int(input("Masukkan Panjang Persegi Panjang: "))
        Lebar = int(input("Masukkan Lebar Persegi Panjang: "))

        Luas = Panjang * Lebar
        print("Luas Persegi Panjang: ", Luas)
    elif pilihan.upper() == "KELILING":
        Panjang = int(input("Masukkan Panjang Persegi Panjang: "))
        Lebar = int(input("Masukkan Lebar Persegi Panjang: "))

        Keliling = 2 * (Panjang + Lebar)
        print("Keliling Persegi Panjang: ", Keliling)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")