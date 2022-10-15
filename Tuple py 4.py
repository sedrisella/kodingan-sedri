from calendar import c


print("        TUPLE                 ")
print("==============================")

numbers=(2,3,4,6,7,8,9,10)
#immutable artinya nilainya tidak bisa diubah ubah,kalo diubah akan terjadi eror
print(numbers[3])

print("        UNPACK               ")
print("==============================")
#cara 1
numbers=(1,2,3,4,5)
x= numbers[0]
y=numbers[1]
z=numbers[2]
a=numbers[3]
b=numbers[4]
print (y)
#cara 2
print("==============================")
numbers=(1,2,3,4,5)
x,y,z,a,b=numbers
print(z)
#cara 3
print("==============================")
numbers=(1,2,3,4,5)
x,*c=numbers
print("")
print(x)
print(c)

