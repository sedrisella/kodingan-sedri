from psutil import users


print("        MENULIS FILE          ")
print("==============================")

users= open("kookie.txt","w")
users.write("saya-saya")

users.close()