#tugas 2
print("\tNama : Sedri sella Jumeni")
h="PROGRAM MENGHITUNG PEMBELIAN"
garis="-"*100
print(h.center(100))
print(garis)

harga=20000
print("Harga satuan     : Rp. "+str(harga))  
Jumlah_pembelian=input("Jumlah pembelian : ")
discon=harga*0.1
print("Discon           : "+str(discon))
harga_total=int(harga)*int(Jumlah_pembelian)-discon
print("Harga Total      : "+str(harga_total))
print("-"*100)

