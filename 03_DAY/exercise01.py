age = 18
height = 1.74
complejo =7j

base = float(input("Escribe base: "))
altura = float(input("Escribe altura: "))
area=0.5*base*altura
print("El area del triangulo es: ", area)

side_a = float(input("Escribe lado a: "))
side_b = float(input("Escribe lado b: "))
side_c = float(input("Escribe lado c: "))
perimetro = side_a + side_b + side_c
print("El perimetro es: ", perimetro)

length = float(input("Length: "))
width = float(input("width: "))
arearect = length*width
perimeter = length+width
print("Area: ", arearect, "Perimeter: ", perimeter)

radius = float(input("radius: "))
pi = 3.14
areacir = pi*(radius**2)
c = pi*2*radius
print("area: ", areacir, "circuferencia: ", c)

slope = 2
y_intercept = -2
x_intercept = 1

print("Pendiente  de la ecuación y = 2x - 2:", slope)
print("Intersección en el eje y :", y_intercept)
print("Intersección en el eje x :", x_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)

print("Pendiente entre los puntos (2, 2) y (6, 10):", slope_points)
print("Distancia euclidiana entre los puntos (2, 2) y (6, 10):", distance)

print("¿Las pendientes son iguales?", slope == slope_points)

def calculate_y(x):
    return x**2 + 6*x + 9

x_values = [-4, -3, 0, 1]
print("Valores de y para diferentes valores de x:")
for x in x_values:
    print(f"x = {x}, y = {calculate_y(x)}")

len_python = len("python")
len_dragon = len("dragon")
print("Longitud de 'python':", len_python)
print("Longitud de 'dragon':", len_dragon)
print("¿Las longitudes son iguales?", len_python == len_dragon)

on = 'on' in 'python' and 'on' in 'dragon'
print("¿'on' está en ambas palabras 'python' y 'dragon'?", on)

sentence = "I hope this course is not full of jargon."
contains_jargon = "jargon" in sentence
print("¿La palabra 'jargon' está en la oración?", contains_jargon)


print("No existe 'on' en ambas palabras 'python' y 'dragon':", not ('on' in 'python' and 'on' in 'dragon'))

len_float = float(len_python)
len_str = str(len_float)
print("Longitud de 'python' convertida a float y luego a string:", len_str)

def is_even(number):
    return number % 2 == 0
print("¿4 es par?", is_even(4))  
print("¿5 es par?", is_even(5))

result = (7 // 3) == int(2.7)
print("¿La división entera de 7 entre 3 es igual al valor de int(2.7)?", result)

resultado = type('10') == type(10)
print("¿El tipo de '10' es igual al tipo de 10?", resultado)

veri = int(9.8) == 10
print("\n¿int('9.8') es igual a 10?", veri)

hours = float(input("Ingrese las horas trabajadas: "))
rate = float(input("Ingrese la tarifa por hora: "))
pay = hours * rate
print("El pago total es: ",pay)

years = float(input("Ingrese el número de años: "))
seconds_in_a_minute = 60
minutes_in_an_hour = 60
hours_in_a_day = 24
days_in_a_year = 365
seconds_in_years = years * days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
print("Una persona que vive",  years ,"años podría vivir aproximadamente: ", seconds_in_years ,"segundos.")

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)