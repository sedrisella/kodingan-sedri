print("=====2. GENERAL EXCEPTION=======")
print("================================")
try :
    level = input(" Level kamu : ")
    level = int(level)
    level=level/0
    print(level)
except:
    print("terjadi kesalahan")