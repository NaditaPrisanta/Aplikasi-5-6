# Konversi dari Jam ke Menit dan Detik

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI KONVERSI DARI JAM KE MENIT DAN DETIK")
print("--------------------------------------------------------------------------------")

while True:
    Jam = int(input("Masukkan Waktu dalam Jam: "))

    # Konversi ke menit
    Menit = Jam * 60

    # Konversi ke detik
    Detik = Jam * 3600

    print("Waktu dalam Menit: ", Menit)
    print("Waktu dalam Detik: ", Detik)

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Ingin Mengkonversi Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break