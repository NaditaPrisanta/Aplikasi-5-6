# Konversi dari jam ke Menit ATAU Detik

print("----------------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENNGKONVERSI DARI JAM KE MENIT ATAU DETIK")
print("-----------------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Konversi ke Menit atau Detik (Menit/Detik): ")

    if pilihan.upper() == "MENIT":
        Jam = int(input("Masukkan Jumlah Jam: "))

        Menit = Jam * 60
        print("Jumlah Menit: ", Menit)
    elif pilihan.upper() == "DETIK":
        Jam = int(input("Masukkan Jumlah Jam: "))

        Detik = Jam * 3600
        print("Jumlah Detik: ", Detik)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Mengkonversi Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")
