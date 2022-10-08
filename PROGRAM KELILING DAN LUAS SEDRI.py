print("""
====================================
PROGRAM MENGHITUNG LUAS DAN KELILING 
         PERSEGI PANJANG
====================================""")

p= int(input("masukkan nilai panjang= "))
l= int(input("masukkan nilai lebar  = "))

luas = p*l
keliling = 2* (p+l)

print("luas persegi panjang adalah     = "+ str(luas))
print("keliling persegi panjang adalah = "+ str(keliling))