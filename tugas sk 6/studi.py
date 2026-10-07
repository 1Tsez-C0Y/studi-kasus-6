import csv

with open('iventaris.csv', mode='a', newline='') as csv_file:
    pass

while True:
    print("\n==Toko Kelontong==")
    print("1. Lihat semua barang")
    print("2. Tambah barang baru")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        Bar = []
        with open('iventaris.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                Bar.append(row)

        if len(Bar) == 0:
            print("\nData masih kosong.")
        else:
            print("\n= Daftar Barang =")
            print("Nama | Jumlah | Harga")
            for row in Bar:
                print(row[0], "|", row[1], "|", row[2])


    elif pilihan == "2":
        nama = input("Nama barang   : ")
        jumlah = input("Jumlah barang : ")
        harga = input("Harga satuan  : ")

        with open('iventaris.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([ nama, jumlah, harga])
        print("\nBarang baru berhasil ditambahkan!")

    elif pilihan == "3":
        print("Terima kasih, program selesai")
        break
    else:
        print("Pilihan tidak valid, coba lagi")