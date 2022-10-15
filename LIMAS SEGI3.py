print("==LIMAS SEGITIGA==")

print("Masukkan alas segitiga:")
a = float(input())
print("Masukkan tinggi segitiga:")
t = float(input())
print("masukkan tinggi Limas:")
l = float(input())
lS1 = a * t / 2
lS2 = a * t / 2
lS3 = a * t / 2
lS4 = a * t / 2
luas = lS1 + lS2 + lS3 + lS4
volume = float(1) / 6 * a * t * l
print("Luas Limas Segitiga:" + str(luas))
print("Volume Limas Segitiga:" + str(volume))
