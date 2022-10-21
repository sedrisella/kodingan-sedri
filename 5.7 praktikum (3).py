print("\t\t\tNama : Sedri sella Jumeni")
print("-"*(50))

a=int(input("Masukan bilangan 1 ="))
b=int(input("Masukan bilangan 2 ="))
c=int(input("Masukan bilangan 3 ="))

if a == b and a == c and b==c:
    print("Nilai ketiga bilangan sama = "+str(a))
elif a==b:
     print("Nilai kedua bilangan sama = "+str(b))

elif a==c:
    print("Nilai kedua bilangan sama = "+str(c))
elif b==c:
    print("Nilai kedua bilangan sama = "+str(c))
else:
    print("bilangan tidak ada yang sama ")