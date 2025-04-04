                                      #Exercises: Level 1
#1 Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count= count + 1

numbers  = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(numbers)

#2 Iterate 10 to 0 using for loop, do the same using while loop.
numberS = [10,9,8,7,6,5,4,3,2,1,0]
for numberS in numbers:
    print(numberS)

count2 = 10
while count2 > 0:
    print(count2)
    count2= count2 - 1


#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
t = 8
for i in range(t):
    for j in range(i):
        print('#', end = '')
    print()

#4 Use nested loops to create the following:
r = 8
for n in range(r):
    print('# '* r)
    
#5 Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
o = 0
for o in range (11):
    print(o, 'x', o, '=', o * o)

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
li = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in li:
    print(item)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
p = 0
if p % 2 == 0:
    for p in range(101):
        print(p)

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range (0, 100, 2):
    print(odd)

                                        #Exercises: Level 2
#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for X in range(1,101):
    nk = X
    suma = suma + nk

print('La suma es: ',suma)

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sumEven = 0
sumOdd= 0
for M in range(1,101):
    if M % 2 ==0:
        sumEven += M
    else:
        sumOdd += M
print('La suma de pares es: ',sumEven)
print('La suma de impares es: ',sumOdd)

                                      #Exercises: Level 3
#1 Go to the data folder and use the countries.py file. Loop through the countries 
# and extract all the countries containing the word land.
import paises_3
for P in paises_3.countries:
    print(P)

#2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for F in reversed(fruits):
    print(F)


#3 Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world

import countries_data as lol
paises = lol.paiSES
idioms = list()
repTdioma=0
for pais in paises:
    for idioma in pais["languages"]:
        if idioma not in idioms:
            idioms.append(idioma)
        else:
            repTdioma+=1

print('El total de idiomas es: ',len(idioms))
print('La repetición de idiomas es de: ',repTdioma)

dcIdm={}
for idioma in idioms:
    dcIdm[idioma]=0

for idioma in dcIdm:
    for pais in paises:
        if idioma in pais["languages"]:
            dcIdm[idioma]+=pais["population"]

menorMayor=sorted(dcIdm.values(),reverse=True)
the10=menorMayor[0:10]

for valor in the10:
    for idioma in dcIdm:
        if valor==dcIdm[idioma]:
            print(idioma,valor)

print('')