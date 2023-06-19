# Hitung Luas dan Keliling Persegi 

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS DAN KELILING PERSEGI")
print("--------------------------------------------------------------------------------")

while True:
    Sisi = int(input("Masukkan Panjang Sisi Persegi: "))

    Luas = Sisi * Sisi
    Keliling = 4 * Sisi

    print("Luas Persegi: ", Luas)
    print("Keliling Persegi: ", Keliling)

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break