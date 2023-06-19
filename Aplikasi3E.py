# Konversi Suhu dari Fahrenheit ke Celcius dan Reamur

print("--------------------------------------------------------------------------------")
print("SELAMAT DATANG DI APLIKASI KONVERSI SUHU DARI FAHRENHEIT KE CELCIUS DAN REAMUR")
print("--------------------------------------------------------------------------------")

while True:
    Fahrenheit = int(input("Masukkan Suhu dalam Fahrenheit: "))

    # Konversi ke Celsius
    Celsius = (Fahrenheit - 32) * 5/9

    # Konversi ke Reamur
    Reamur = (Fahrenheit - 32) * 4/9

    print("Suhu dalam Celsius: ", Celsius)
    print("Suhu dalam Reamur: ", Reamur)

    print("---------------------------------------------------------------------------------")
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI INI")
    print("----------------------------------------------------------------------------------")

    Pilih = input("Ingin Mengkonversi Lagi? (YES/NO): ")
    if Pilih.upper() != "YES":
        break