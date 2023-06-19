# Konversi Suhu dari Fahrenheit ke Celcius ATAU Reamur

print("----------------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI PENNGKONVERSI SUHU DARI FAHRENHEIT KE CELCIUS ATAU REAMUR")
print("-----------------------------------------------------------------------------------------")

while True:
    pilihan = input("Pilih Konversi ke Celsius atau Reamur (c/r): ")

    if pilihan.upper() == "CELCIUS":
        Fahrenheit = int(input("Masukkan Suhu dalam Fahrenheit: "))

        Celsius = (Fahrenheit - 32) * 5/9
        print("Suhu dalam Celsius: ", Celsius)
    elif pilihan.upper() == "REAMUR":
        Fahrenheit = int(input("Masukkan Suhu dalam Fahrenheit: "))

        Reamur = (Fahrenheit - 32) * 4/9
        print("Suhu dalam Reamur: ", Reamur)
    else:
        print("Pilihan Tidak Valid!")

    Pilih = input("Ingin Mengkonversi Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")