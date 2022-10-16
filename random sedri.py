print ("====RANDOM====")
import random

users  = ["sedri","melati","mawar","sasa","zelda","sindi"]

batas_bawah=0
batas_atas=len(users)-1

random_int = random.randint(batas_bawah,batas_atas)

winner=users[random_int]
print (winner)
