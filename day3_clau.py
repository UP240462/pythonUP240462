#3 DAY THREE UP240462 CLAUDIA
jahr = int(input("Bitte geben Sie ein Jahr ein: ")) # Eingabe des Jahres
Körpergröße = float(input("Write your height: ")) # Körpergröße in Metern
complexNumber = complex(input("Write a complex number: ")) # Eingabe einer komplexen Zahl

#4 Triangle
base = int(input("Enter the base of the triangle: ")) # Eingabe der Basis des Dreiecks
height = int(input("Enter the height of the triangle: ")) # Eingabe der Höhe des Dreiecks
area1 = 0.5 * base * height 
print("The area of the triangle is: ", area1)

#5 Perimeter of a triangle
sideA = int(input("Enter the measure of sideA: ")) # Eingabe der Länge der Seite a
sideB = int(input("Enter the measure of sideB: ")) # Eingabe der Länge der Seite b
sideC = int(input("Enter the measure of sideC: ")) # Eingabe der Länge der Seite c
perimeter1 = sideA + sideB + sideC 
print("The perimeter of the triangle is: ", perimeter1)

#6 Rectangle area and perimeter
width = int(input("Enter the measure of the width of the rectangle: ")) # Eingabe der Breite des Rechtecks
leght = int(input("Enter the measure of the leght of the rectangle: ")) # Eingabe der Länge des Rechtecks
area2 = width * leght 
perimeter2 = 2 * (width + leght)
print("The are of the rectangle is: ", area2)
print("and the perimeter is: ", perimeter2)

#7 Circle
r = float(input("Enter the radius of the circle: ")) # Eingabe des Radius des Kreises
area3 = 3.14159 * r**2 
circunference = 2 * 3.14159 * r
print("The area is: ", area3)
print("and the circunference is: ", circunference)

#8 Slope
# la pendiente de "y = 2x -2"
pendiente1 = 2 # la pendiente de la ecuación
intY = -2 # la intersección con el eje y
intX = intY / pendiente1 # la intersección con el eje x
print("La pendiente de la ecuación es: ", pendiente1)
print("La intersección con el eje x es: ", intX)

#9 Eucleadian distance between point (2,2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("The distance between the two points is: ", distance)
slope = (y2 - y1) / (x2 - x1)
print("The slope is: ", slope)

#10 Compare the slopes in tasks 8 and 9
pendiente1< slope
if True:
    print("The slope is greater than pendiente1")
else:
    print("The slope is less than pendiente1")

#11 Calculate the value of y (y = x^2 + 6x + 9) 
ex = int(input("Enter the value of ex: "))
y = (ex**2 + 6*ex + 9)
print("The value of y is: ", y)

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement
word1 = "python"
word2 = "dragon"
longitud1 = len(word1)
longitud2 = len(word2)
print("Longitud de python es: ", longitud1)
print("Longitud de dragon es: ", longitud2)

if longitud1 > longitud2:
    print("'python' es más largo que 'dragon'")
print("'dragon' es más largo que 'python'")


#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
on = ("python","dragon")
#contiene 'on' en dragon y python?
if "dragon" in on:
    print("on is in dragon")
if "python" in on:                                                       
    print("on is in python")

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("jargon is in the sentence")

#16 Find the length of the text python and convert the value to float and convert it to string
word = "python"
long = len(word)
float(int(long))
str(int(long))
print("The lenght of 'puthon' is: ", long)                                                  
print("The lenght of 'python' is: ", long)

#17 Par o impar
numero = int(input("Dame un número: "))
if numero%2==0:
    print("El número es par")
else:
    print("El numero es impar")

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floDiv = 7 // 3 
entero = int(2.7)
if floDiv is entero:
    print("Is equal")

#19 Check if type of '10' is equal to type of 10
n = '10'
n2 = 10
if  n is n2:
    print("Is the same")
print("Is not the same")  

#20 Check if int('9.8') is equal to 10
a = int(9.8)
print(int(9.8))
a2 = 10
if a is a2:
    print("Is equal")
print("Is not equal")

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
day = hour * rate
week = day * 7
print("Your weekly earning is: ", week, "pesos")

#22 Write a script that prompts the user to enter number of years
years = 100
seconds = 3600 * 24
week = 7 * seconds
total = week * years
print("You have lived for: ", total, "seconds")

#23 Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
