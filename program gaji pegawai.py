print("Nama : Sedri sella Jumeni")
judul="PROGRAM GAJI PEGAWAI"
print(judul.center(50))

nama=input("Nama Karyawan :")
gaji_pokok=float(input("Gaji Pokok :"))
anak=int(input("jumlah anak :"))

tunjangan_kesejateraan=gaji_pokok*20/100
tunjangan_keluarga=(gaji_pokok*10/100)*anak
gaji_kotor=gaji_pokok+tunjangan_kesejateraan+tunjangan_keluarga
pajak=gaji_kotor*10/100
print("-"*(50))
print("Gaji Pokok\t T.Kesejateraan \t T.Keluarga\t Pajak")
print(f"{gaji_pokok}\t\t{tunjangan_kesejateraan}\t\t{tunjangan_keluarga}\t\t{pajak}")
print("-"*(50))
print("Gaji Kotor :"+str(gaji_kotor))
print("Gaji Bersih:"+str(pajak))


