jdl="PROGRAM MENGHITUNG TAGIHAN TELEPON"
print(jdl.center(50))
garis="-"*100
print(garis)

print("\tDATA PELANGGAN")
nama_pelanggan=input("\tNama Pelanggan \t:")
Percakapan=float(input("\tPercakapan \t:"))
sms=float(input("\tSMS \t\t: "))

print("\tTAGIHAN")
abonemen=20000
becak=Percakapan*1000
besem=sms*300
total_tagihan=abonemen+becak+besem

print(f"\tAbonemen \t\t: {abonemen}")
print(f"\tBiaya percakapan \t:{becak}")
print(f"\tBiaya SMA \t\t:{besem}")
print(f"\tTotal Tagihan \t\t:{total_tagihan}")
print("-"*50)




