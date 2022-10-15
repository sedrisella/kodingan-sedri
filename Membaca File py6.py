#membaca data file txt
#apend artinya menambahkan data ke file yang sudah ada
#writen artinya membaca data yang sudah ada
#r+ membaca dan menulis
print("      Membaca file            ")
print("==============================")
users = open("kookie.txt","r")
print(users.read())
users.close()

print("==============================")
users = open("kookie.txt","r")
print(users.readline())
print(users.readline())
print(users.readline())

users.close()
print("==============================")
users = open("kookie.txt","r")
array = users.readlines()
print(array)
users.close()
print("==============================")