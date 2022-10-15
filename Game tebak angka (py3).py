print("      GAME TEBAK ANGKA       ")
print("==============================")

trying=0
angka_rahasia =6
limit =3

while trying< limit :
    gues_number = input ("Masukan angka tebakan anda (1-9) : ")
    gues_number =int(gues_number)

    if gues_number==angka_rahasia:
        print("Selamat,Tebakan anda Benar")
        break #perulangan akan ditutup secara paksa,walaupun syaratnya belum terpenuhi
    
    trying=trying + 1
    print("==============================")
