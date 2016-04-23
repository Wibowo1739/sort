#Bubble sort
#numbers = input("Enter 10 numbers seperated by a space: ")
sort = []
num = []
numbers = "5 4 8 3 1 2 6 9 10 7 7" #stub
numbers = numbers.split()
for n in numbers:
    num.append(int(n))
lennum = len(num)

print("Original")
print(num)
print()
print("Sorting")

for j in range(0,lennum):
    temp = int(num[0])+1 #always bigger than first number to start the loop
    for i in range(0,lennum):
        compare = int(num[i])
        if temp > compare: #comparing the smaller one
            temp = compare
    sort.reverse()
    sort.append(temp)
    sort.reverse()
    num.remove(temp)
    print(num+sort)
    lennum = len(num)


print()
print("Sorted")
print(sort)