
#print()#dipakai untuk mencetak tulisan tulisan ke terminal program kita
#input()#gunanya untuk menampilkan teks ,menangkap imputan dari user dan disimpan ke variabel
from unittest import result


print("=====     FUNGSI     =========")
print("==============================")
def halo_semua():
    print ("halo semua")
    print("selamat belajar pyhton")
print("start")
halo_semua()
print("finish")
print("==============================")
print("=====PARAMETER FUNGSI=========")

def halo_user (name,level):
    print (f"halo {name}-{level}")
    print("selamat belajar pyhton")
print("start")
halo_user("sedri",10)
print("==============")
halo_user("jungkook",8)
print("finish")

print("==============================")
print("=====Keyword Argument=========")

def halo_kok (name,level):
    print (f"halo {name}-{level}")
    print("selamat belajar pyhton")
print("start")
halo_kok(level=10,name="sedri")
print("finish")

print("==============================")
print("========Return Value=========")
 #input
def halo_king (a,b):
     #proses
    return a*b
    #output
result=halo_king(2,9)
print(result) #hasilyang diinginkan adalah 2*9=18
    




