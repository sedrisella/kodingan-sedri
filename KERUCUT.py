print("==KERUCUT==")

print("Masukan panjang sisi:")
s = float(input())
print("Masukan jari-jari:")
r = float(input())
print("Masukan tinggi kerucut:")
t = float(input())
ls = 3.14 * r * s
lp = 3.14 * r * s + 3.14 * r * r
volume = float(1) / 3 * 3.14 * r * r * t
print("Luas selimut kerucut adalah:" + str(ls))
print("Luas permukaan kerucut:" + str(lp))
print("Volume kerucut adalah:" + str(volume))
