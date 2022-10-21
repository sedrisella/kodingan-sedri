judul="DATA PEGAWAI"
print(judul.center(50))
print("-"*(50))


nama=input("\t\tNama\t       :")
golongan=str(input("\t\tGolongan       :"))
t_jam_kerja=float(input("\t\tTotal Jam Kerja:"))

if golongan=="A" :
    gaji_pokok=500000
elif golongan=="B":
    gaji_pokok=700000
elif golongan=="C":
    gaji_pokok=900000
else:
    print("Golongan yang anda masukan tidak terdaftar")

##TUNJANGAN
if golongan=="A" :
    tunjangan=10/100*gaji_pokok
elif golongan=="B":  
    tunjangan=15/100*gaji_pokok
elif golongan=="C":
    tunjangan=10/100*gaji_pokok
else:
    tunjangan=0

##LEMBUR
if golongan=="A" :
    lembur=5000
elif golongan=="B":
    lembur=10000
elif golongan=="C":
    lembur=5000
else:
    print("anda tidak menganbil lembur")
print("-"*(50))

judul="PERHITUNGAN GAJI"
print(judul.center(50))
print("-"*(50))


gaji=gaji_pokok+tunjangan+lembur

print("\t\tgaji pokok:"+str(gaji_pokok))
print("\t\tTunjangan :"+str(tunjangan))
print("\t\tLembur    :"+str(lembur))
print("-"*(50))
print("\t\tTotal :"+str(gaji))


print("\t\t\tNama : Sedri sella Jumeni")