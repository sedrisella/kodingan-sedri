print("    MENGHITUNG DEBIT AIR TERJUN KONSEP 2     ")
print("======================================")

print("Berapakah debit air terjunnya :" + "   m3/detik")
debit = int(input())
print("Berapa lama waktu yang dibutuhkan :" + "  menit")
t = int(input())
waktu = t * 60
volume = debit * waktu
print("volume air yang bisa dipindahkan dalam waktu tersebut :" + str(volume) + "  m3")
print("======================================")