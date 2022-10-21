a=int(input("Nilai A: "))
b=int(input("Nilai B: "))
jml=0
for i in range(a, b):
    print(i+1, " ", end="")
    jml=jml+i+1
    if i == b-2:
        break
print()
print(jml)