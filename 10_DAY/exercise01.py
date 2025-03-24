#1
numbers = (0, 1, 2, 3, 4, 5,6,7,8,9,10)
for number in numbers:
    print(number)
count = 0
while count < 11:
    print(count)
    count = count + 1
#2
numbers = (10,9,8,7,6,5,4,3,2,1,0)
for number in numbers:
    print(number)
i = 10
while i >= 0:
    print(i)
    i = i -1 
#3
for i in range(1, 8):  
    print('#' * i)
#4
for i in range(8):  
    for j in range(8): 
        print('#', end=' ') 
    print()  
#5
for i in range (11):
    print(f"{i} x {i} = {i * i}")
#6
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lst in lst:
    print(lst)
#7
for n in range(0,101,2):
    print(n)
#8
for m in range(1,101,2): 
    print(m)
    