#1
dog = {}

#2
dog["name"], dog["color"], dog["breed"], dog["legs"], dog["age"] = "Tobby", "white", "Dachshund", 4, 5   
print(dog)

#3
student = {                                           
    "first_name":"Benjamin",
    "last_name":"Gonzalez  ",
    "gender":"male",
    "age":18,
    "marital_status":"single",
    "skills":["soccer", "sleeping", "math"],
    "country":"Mexico",
    "city":"Aguascalientes",
    "address":"Flor de Nochebuena #84"
}

#4
print(len(student))                                                 

#5
print(student["skills"])                                            
print(type(student["skills"]))

#6
student['skills'].append('drawing')                                 

#7
print(list(student.keys()))                                         

#8
print(list(student.values()))                                       

#9
print(student.items())                                              

#10
del student["marital_status"]                                       

#11
del student 