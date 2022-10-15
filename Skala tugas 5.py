#KONSEP SATU
print("    MENGHITUNG SKALA KONSEP 1     ")
print("======================================")

jsebenarnya = 220 * 1000000
print("Jarak sebenarnya di konversikan ke cm terlebih dahulu yaitu 220 km =" + str(jsebenarnya) + "cm")
sekala = float(jsebenarnya) / 10
print("Jadi sekalanya dalam cm adalah :1:" + str(sekala))

print("======================================")

#KONSEP DUA
print("    MENGHITUNG SKALA KONSEP 2     ")
print("======================================")

print("Masukan jarak sebenarnya :" + "  km")
a = int(input())
jsebenarnya = a * 100000
print("Masukan jarak pada peta :" + " cm")
jpeta = int(input())
skala = float(jsebenarnya) / jpeta
print("Jadi sekala dalam cm adalah : 1 :" + str(skala))
