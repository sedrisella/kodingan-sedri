import os

print("""
Welcome to Game Tebak Nama 
>---------------------------<\n
Selamat bermain:)

Daftar nama : Septi, Bayu, Budi, Tono, Dika, Danu, Anto, Elga, Safi
Pemain 1: Buatlah nama tersembunyi dari nama nama diatas!!\n
""")
tersembunyi=str(input("Masukkan Nama tersembunyi yang akan di tebak oleh pemain 2 : "))
os.system('cls')

print("""
-------------------------------------------------------------------
Pemain 1 sudah membuat nama yang akan anda tebak, silahkan ditebak """)
batas=3
for percobaan in range(batas):
    jawaban=str(input(f"Silahkan Masukkan tebakanmu : "))
    if jawaban == tersembunyi:
        print("Conglatulation jawabanmu bener bangettt")
        break
    else:
        print(f"sorry, coba lagi...\nSemangat yah masih {percobaan+1}x tebak aja udh nyerah sih")
if percobaan == batas-1:
    print("huuuuuuu,,,yang sabar yah kawann")