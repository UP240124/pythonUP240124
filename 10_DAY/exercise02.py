#1
sum = 0
for n in range(0,101,1):
    sum = n+sum
    print(sum)
#2
odd_sum = 0
even_sum = 0
for n in range(0,101,2):
    odd_sum=n+odd_sum
    print(odd_sum)
for n in range(1,101,2):
    even_sum=n+even_sum
    print(even_sum)
    