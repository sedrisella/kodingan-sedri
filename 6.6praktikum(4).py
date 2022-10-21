x=int(input("Masukkan nilai :"))
y=int(input("Masukkan pangkat :"))
jumlah=1
for i in range(y):
    jumlah=jumlah*x

print(f"{x}^{y}={jumlah}")