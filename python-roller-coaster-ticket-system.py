print("=== Pengecekan Tiket Roller Coaster")

umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
harga = 50000

# Kondisi IF pertama
if umur >= 12:

    # Nested IF pertama
    if tinggi >= 150:
        print("\nSyarat terpenuhi, anda diperbolehkan naik!")
        member = input("Punya member? (y/t): ")

        # Nested IF kedua
        if member == "y":
            harga -= 10000
            print("Anda dapat diskon 10K!")

        print("total tiket: Rp ", harga)
        uang = int(input("Masukkan uang anda: Rp "))

        if uang == harga:
            print("Uang anda pas!")
        elif uang > harga:
            print("Kembalian anda Rp: ", uang - harga)
        else:
            print("Uang anda kurang Rp: ", harga - uang)
    else:
        print("Tinggi anda belum mencukupi, tidak boleh masuk!")
else:
    print("Anda belum cukup umur!")
