print("          LIST  METHOD       ")
print("==============================")
numbers=[5,6,7,8,2]
print(numbers)
numbers.append(40)#append digunakan untuk menambah elemen di dalam list
print(numbers)
print("==============================")
numbers.insert(3,9)
print(numbers)

#membuang/menghapus index dan elemen
numbers.pop(4)
print (numbers)

numbers.remove(9)
print(numbers)

#mengurutkan elemen
numbers.sort()
print(numbers)
