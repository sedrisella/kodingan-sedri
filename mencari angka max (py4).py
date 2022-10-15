print("           MENCARI ANGKA MAX             ")
print("========================================")
numbers=[2,3,5,6,7,9,10]

total= sum(numbers)
print(total)
print("========================================")
#MENCARI ANGKA YANG PALING BESAR NILAINYA(1)
numbers=[2,3,5,6,7,9,10]
max_numbers = max(numbers)
print(max_numbers)
print("========================================")
#MENCARI ANGKA YANG PALING BESAR NILAINYA(2)
numbers=[2,3,5,6,7,9,10]
numbers.sort()
max_numbers=numbers[-1]
print(max_numbers)
print("========================================")
#MENCARI ANGKA YANG PALING BESAR NILAINYA(3)
numbers=[2,3,5,6,7,9,10]
max_numbers=numbers[0]
for number in numbers :
    if number>max_numbers:
        max_numbers=number
print (max_numbers)
