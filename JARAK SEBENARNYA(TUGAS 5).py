print("    MENGHITUNG JARAK SEBENARNYA KONSEP 1     ")
print("=============================================")

jsebenarnya = 20 * 5000000
print("Jadi jarak sebenarnya dari seteng ke labuan badas adalah :" + str(jsebenarnya) + "  cm")
konversi = float(jsebenarnya) / 100000
print("Jadi jarak sebenarnya dalam satuan km adalah :" + str(konversi) + " km")
print("=============================================")
#KONSEP 2
print("    MENGHITUNG JARAK SEBENARNYA KONSEP 2     ")
print("=============================================")

print("Masukan skala : 1 : ")
skala = int(input())
print("Masukan Jarak pada peta:" + "  cm")
jpeta = int(input())
jsebenarnya = jpeta * skala
print("Jarak sebenarnya dari seteng ke labuan badas adalah :" + str(jsebenarnya) + " cm")
konversi = float(jsebenarnya) / 100000
print("Jarak sebenarnya dari seteng ke labuan badas adalah :" + str(konversi) + " km")

print("=============================================")