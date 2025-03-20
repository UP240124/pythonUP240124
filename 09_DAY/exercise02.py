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