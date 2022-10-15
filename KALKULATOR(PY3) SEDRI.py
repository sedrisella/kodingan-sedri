print("      APLIKASI KALKULATOR SEDERHANA       ")
print("==========================================")

#operasi yang di support (+,-,*,/,keluar)
operasi =  ""

while operasi != " exit ":
    operasi=input ("Pilih operasi yang anda inginkan : ")

    if operasi == "keluar":
     break

    if operasi !="+" and operasi !="-" and operasi !="*" and operasi !="/" :
      print ("Perinta tidak dikenal")
      #continue

    a=int(input ("Masukan angka pertama : "))
    b=int(input ("Masukan angka kedua   : "))

    if operasi=="+":
      result= a+b
    elif operasi=="-":
      result= a-b
    elif operasi=="*":
      result= a*b
    elif operasi=="/":
      result= a/b
    
    print(f"hasil :{result}" )

print("Terima kasih sudah menggunakan aplikasi ini")