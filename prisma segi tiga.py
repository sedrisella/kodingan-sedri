print("==PRISMA SEGI TIGA==")

print("Masukan nilai sisi pertama:")
s1 = float(input())
print("Masukan nilai sisi kedua:")
s2 = float(input())
print("Masukan nilai sisi ketiga:")
s3 = float(input())
print("Masukan tinggi prisma:")
t = float(input())
print("Masukan alas segitiga:")
a = float(input())
print("Masukan tinggi segitiga:")
tinggi = float(input())
luas = (s1 + s2 + s3) * t + a * tinggi
volume = float(1) / 2 * a * tinggi * t
print("Luas prisma segitiga adalah:" + str(luas))
print("Volume prisma segitiga :" + str(volume))
