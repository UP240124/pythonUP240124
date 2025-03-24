#1
score = int(input("Enter your score: "))
if score >= 80 and score<=100:
    print("Your grade is an A")
elif score >= 70 and score<=89:
    print("Your grade is an B")
elif score >= 60 and score<=69:
    print("Your grades is an C")
elif score >= 50 and score<=59:
    print("Your grades is an D")
elif score >= 0 and score<=49:
    print("Your grades is an F")

#2
month = str(input("Enter any month : "))
if month == ["September", "October","November"]:
    print(f"The season of {month} is Autumn")
elif month == ["December" , "January" , "February"]:
    print(f"The season of {month} is Winter")
elif month == ["March" ,"April" , "May"]:
    print(f"The season of {month} is Spring")
elif month == ["June" , "July" , "August"]:
    print(f"The season of {month} is Summer")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_add = input("Enter a fruit to add: ").lower()
if fruit_to_add in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_add)
    print("Modified list:", fruits)

    