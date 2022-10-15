print("==============================")
print("      OPERATOR LOGIKA         ")
print("==============================")
#PENGGABUNGAN OPERATOR LOGIKA DENGAN IF STATE
name = " Sedri sella jumeni "
if len(name)> 4 :
    print("selamat nama anda panjang")
else:
    print("nama anda terlalu pendek")
print("==============================")
name = " Sedri sella jumeni "
if len(name)> 4 or True: #jika ada kondisi false or true maka kondisi yang dijalankan adalah true
    print("selamat nama anda panjang") #tetapi jika kondisinya false and true maka yang dijalankan adalah false
else:
    print("nama anda terlalu pendek")
print("==============================")
name = " Sedri sella jumeni "
if len(name)> 4 and False: #jika ada kondisi false or true maka kondisi yang dijalankan adalah true
    print("selamat nama anda panjang") #tetapi jika kondisinya false and true maka yang dijalankan adalah false
else:
    print("nama anda terlalu pendek")
print("==============================")
name = " Sedri sella jumeni "
by_pass_validation = False
if len(name)> 5  or by_pass_validation: #dia akan tetap mencetak selamat nama anda panjang karena len namenya >5 walaupun
    print("selamat nama anda panjang")#di var by pass validationnya bernilai false
else:
    print("nama anda terlalu pendek")
print("==============================")