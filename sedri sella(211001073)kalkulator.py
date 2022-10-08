# Program kalkulator sederhana
# pertambahan, pengurangan, perkalian, dan pembagian

print("Pilih Opsi Operasi Yang Anda Inginkan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Exit")


pemilihan = float(input("Masukkan Pilihan operasi yang anda inginkan (1/2/3/4/5):"))

if pemilihan == 1:
    bilpertama = float(input("Masukkan bilangan pertama:"))
    bilkedua = float(input("Masukkan bilangan kedua:"))
    jumlah = bilpertama + bilkedua
    print(bilpertama,"+",bilkedua,"=",jumlah)
elif pemilihan == 2:
    bilpertama = float(input("Masukkan bilangan pertama:"))
    bilkedua = float(input("Masukkan bilangan kedua:"))
    kurang = bilpertama - bilkedua
    print(bilpertama,"-",bilkedua,"=",kurang)
elif pemilihan == 3:
    bilpertama = float(input("Masukkan bilangan pertama:"))
    bilkedua = float(input("Masukkan bilangan kedua:"))
    kali = bilpertama * bilkedua
    print(bilpertama, "x", bilkedua, "=", kali)
elif pemilihan == 4:
    bilpertama = float(input("Masukkan bilangan pertama:"))
    bilkedua = float(input("Masukkan bilangan kedua:"))
    bagi = bilpertama / bilkedua
    print(bilpertama, "/", bilkedua, "=", bagi)

elif pemilihan == 0:
    print("Program anda Keluar")
else:
    print("Perintah tidak dikenali program ")
print("Program Finish")


