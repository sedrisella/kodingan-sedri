#user=
print("            DICTIONARY             ")
print("===================================")
user={
   "nama":"sedri sella jumeni",
   "age": 19,
   "is_admin": False
}
name=user["nama"]
print("")
print(name)
print("===================================")
user={
   "nama":"sedri sella jumeni",
   "age": 19,
   "is_admin": True
}
user["username"]="sedri_sella_jumeni"
temp=user.get("username","sedri sella jumeni")

#none adalah sebuah tipe data yang menggambarkan bahwa sesuatu itu tidak ada
print("")
print(temp)