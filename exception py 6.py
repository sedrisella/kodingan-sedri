print("=====   1. EXCEPTION   =========")
print("================================")

try :
    level = input(" level kamu : ")
    level = int(level)
    print(level)
except ZeroDivisionError:
    print("Error,itu tidak bisa dibagi 0")
except ValueError:
    print("Yang kamu masukan itu bukan angka")

print("=====2. GENERAL EXCEPTION=======")
print("================================")
try :
    level = input(" Level kamu : ")
    level = int(level)
    level=level/0
    print(level)
except:
    print("terjadi kesalahan")

    

