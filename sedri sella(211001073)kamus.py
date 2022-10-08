#Penerjemah bahasa indonesia ke bahasa sumbawa

print("""
==============================================
        WELCOME TO KAMUS BAHASA SUMBAWA
                -SILAMO-
==============================================
""")
 
Indo_to_Sumbawa = {'saya' : 'kaji', 'kamu' : 'sia','mandi' : 'maning','makan' : 'mangan','tidur' : 'tunung'}
penerjemah=input("Silahkan masukan kata yang ingin anda terjemahkan: ")
if penerjemah=='saya':
    print(f"Saya : {Indo_to_Sumbawa['saya']}")
elif penerjemah=='kamu':
    print(f"Kamu : {Indo_to_Sumbawa['kamu']}")
elif penerjemah=='mandi':
    print(f"Mandi : {Indo_to_Sumbawa['mandi']}")
elif penerjemah=='makan':
    print(f"Makan : {Indo_to_Sumbawa['makan']}")
elif penerjemah=='tidur':
    print(f"Tidur : {Indo_to_Sumbawa['tidur']}")
else:
    print("Tolong periksa kembali kata yang anda masukan")