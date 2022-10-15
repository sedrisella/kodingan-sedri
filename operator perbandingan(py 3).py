#operator perbandingan
#operator Lebih besar/kurang dari
print("============================")
print("   OPERATOR PERBANDINGAN ")
print("============================")


result = 7 > 3  #dia akan menhasilkan true/benar karena benar 7 itu lebih besar dari 3
print(result)

result = 7 < 3  #dia akan menhasilkan false/salah karena benar 7 itu lebih besar dari 3
print(result)

#operator lebih besar sama dengan/lebih kecil sama dengan
result = 6 >=5  #apakah 6 lebih besar sama dengan 5 
print(result)

result = 6 ==5 #apakah 6 sama dengan 5 jawabnnya adalah false karena 6 tidak sama dengan 5
print(result)

result = 6 !=5 #apakah 6 tidak sama dengan 5 jawabannya true karena 6 tidak sama dengan 5
print(result)

#operator perbandingan dengan if
print("===================================")
print("  OPERATOR PERBANDINGAN DENGAN IF ")
print("===================================")

nilai =9

if nilai >=8:
    print("nilai adalah kamu A")
elif nilai>=7:
    print("nilai kamu adalah B") 
elif nilai >=6:
    print("nilai kamu adalah C")
else:
    print("Semangat lagi belajarnya")

print("===================================")
