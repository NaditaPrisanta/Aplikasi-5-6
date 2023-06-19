# Hitung Luas atau Keliling Persegi 

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENGHITUNG LUAS ATAU KELILING DARI PERSEGI")
print("--------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Luas atau Keliling (Luas/Keliling): ")

    if pilihan.upper() == "LUAS":
        Sisi = int(input("Masukkan Panjang Sisi Persegi: "))

        Luas = Sisi * Sisi
        print("Luas Persegi: ", Luas)
    elif pilihan.upper() == "KELILING":
        Sisi = int(input("Masukkan Panjang Sisi Persegi: "))

        Keliling = 4 * Sisi
        print("Keliling Persegi: ", Keliling)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Menghitung Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break
    
    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")