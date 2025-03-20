#1
age = input("Enter your age: ")
if int(age) >= 18:
    print("You´re old enough to learn to drive")
else:
    gap = 18- int(age)
    print(f"You need {gap} more years to learn to drive")

#2
my_age = int(input("Enter your age: "))
your_age = int(input("Enter your age: "))
gap_ages= abs(my_age-your_age)
if my_age == your_age:
    print("We´re both the same age")
elif my_age > your_age:
    if gap_ages==1:
        print(f"I´m {gap_ages} year older than you")
    else:
        print(f"I´m {gap_ages} years older than you")
else:
    if gap_ages == 1:
        print("You´re 1 year older than me")
    else:
        print(f"You´re {gap_ages} years older than me")
    
#3
a = int(input("Enter number a :"))
b = int(input("Enter number b :"))
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")