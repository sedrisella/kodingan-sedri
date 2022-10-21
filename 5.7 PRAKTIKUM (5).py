
judul="DATA NILAI MAHASISWA"
print(judul.center(50))
print("-"*(50))

nama=input("\tNama  :")
Tugas=float(input("\tTugas :"))
UTS=float(input("\tUTS   :"))
UAS=float(input("\tUAS   :"))
print("-"*(50))
judul="NILAI AKHIR DAN GRADE"
print(judul.center(50))
print("-"*(50))
print("\tNama:"+str(nama))
Nilai_akhir=25/100*Tugas+35/100*UTS+40/100*UAS
print("\tNilai Akhir:"+str(Nilai_akhir))

if Nilai_akhir >= 75 :
    grade="A"
elif Nilai_akhir <75 :
    grade="B"
elif Nilai_akhir <60 :
    grade="C"
else:
    grade="E"
print("\tGrade:"+str(grade))
print("-"*(50))
print("\t\t\tNama : Sedri sella Jumeni")

    








