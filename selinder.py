print("==SELINDER==")

print("Masukan jari-jari:")
r = float(input())
print("Masukan tinggi tabung :")
t = float(input())
ls = 2 * 3.14 * r * t
lp = 2 * 3.14 * r * t + 2 * 3.14 * r * r
volume = 3.14 * r * r * t
print("Luas selimut tabung adalah:" + str(ls))
print("Luas permukaan tabung adalah :" + str(lp))
print("Volume tabung adalah:" + str(volume))
