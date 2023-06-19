# Hitung Luas atau Keliling Segitiga

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS ATAU KELILING DARI SEGITIGA")
print("--------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Luas atau Keliling (Luas/Keliling ): ")

    if pilihan.upper() == "LUAS":
        Alas = int(input("Masukkan Panjang Alas Segitiga: "))
        Tinggi = int(input("Masukkan Tinggi Segitiga: "))

        Luas = 0.5 * Alas * Tinggi
        print("Luas Segitiga: ", Luas)
    elif pilihan.upper() == "KELILING":
        Sisi1 = int(input("Masukkan Panjang Sisi1: "))
        Sisi2 = int(input("Masukkan Panjang Sisi2: "))
        Sisi3 = int(input("Masukkan Panjang Sisi3: "))

        Keliling = Sisi1 + Sisi2 + Sisi3
        print("Keliling Segitiga: ", Keliling)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")