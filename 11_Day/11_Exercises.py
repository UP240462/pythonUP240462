'''
                                         #Exercises: Level 1
#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def addTwoNumbers():
    num1 = 56
    num2 = 78
    total = num1 + num2
    print(f'La suma es {total}')
addTwoNumbers()

#2 Area of a circle is calculated as follows: area = π x r x r.
#  Write a function that calculates area_of_circle.
def areaCircle():
    p = 3.1416
    r = 12
    area = p * r *r
    print(f'The area of a circle of 12 radio is {area}')
areaCircle()

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
def addAllNumbers(*args):
    return sum(args) if all(isinstance(i, (int, float))for i in args) else 'Only number values'
print(addAllNumbers(1,2,3,4.5))#10.5
print(addAllNumbers(8,'hola',89)) #'Only number values'

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convertCtoF (celsius):
    fahr= (celsius * 9/5) + 32
    return f'{celsius} grades to Fahrenheit is {fahr}'
print(convertCtoF(35))

#5 Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
month = input('Enter a month: ')
yesmonth= month.capitalize()
aut = ['September', 'October', 'November']
win = ['December', 'January', 'February']
spr = ['March', 'April', 'May']
sum = ['June', 'July', 'August']

def chekcSeason(yesmonth):
    if yesmonth in aut:
        return 'The season is Autumn'
    elif yesmonth in win:
        return 'The season is Winter'
    elif yesmonth in spr:
        return 'The season is Spring'
    else:
        return 'The season is Summer'
print(chekcSeason(yesmonth))

#6 Write a function called calculate_slope which return the slope of a linear equation.
x1= int(input('Enter x1: '))
y1= int(input('Enter y1: '))
x2= int(input('Enter x2: '))
y2= int(input('Enter y2: '))
def calSlope(x1, y1, x2, y2):
    m=(y2-y1)/(x2-x1)
    return f'The slope of the linear equation is {m}'
print(calSlope(x1, y1, x2, y2))

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
b =int(input('Enter the value of b: '))
a =int(input('Enter the value of a: '))
c =int(input('Enter the value of c: '))
def solveQEqn(a,b,c):
    x1= (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2= (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return f'The solution set of the quadratic equation is {x1} and {x2}'
print(solveQEqn(a,b,c))

#8 Declare a function named print_list. It takes a list as a parameter and it prints 
# out each element of the list.
Lista = ['pera','mango','manzana','uva']
def printList(list):
    for i in list:
        print(i)
print(printList(Lista))

#9 Declare a function named reverse_list. It takes an array as a parameter and it 
# returns the reverse of the array (use loops).
pedro = [1,2,3,4,5]
li=['A','B','C','D']
def reverseList(pedro):
    for val in reversed(pedro):
        print(val)
print(reverseList(pedro))
print(reverseList(li))

#10 Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalizeListItems(bob):
    for b in bob:
        print(b.capitalize())
print(capitalizeListItems(['lluvia','pintura','celular','agua','papel']))

#11 Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def addItem(pop,item):
    pop.append(item)
    return pop
print(addItem(['miel','loop','heart'],'pain'))

#12 Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def removeItem(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
numbers= [1,2,3,2,4]
food=['mango','grapes','banana','lemon','piña']
print(removeItem(numbers, 2))
print(removeItem(food, 'banana'))

#13 Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sumOfNumbers(n):
    return sum(range(1,n+1))
print(sumOfNumbers(5)) #suma los numeros del 1 al 5 de uno en 1

#14 Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sumOfOdds(o):
    return sum(num for num in range(1,o+1)if num %2!=0)
print(sumOfOdds(10)) #suma los impares qeu hat del 1 al 10

#15 Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.
def sumOfEven(e):
    return sum(num for num in range(1,e+1)if num %2==0)
print(sumOfEven(10)) #suma los pares que hay del 1 al 10

                                             #Exercises: Level 2
#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and
#  it counts number of evens and odds in the number.
def evenAndOdds(u):
    if not isinstance(u,int) or u<=0:
        return'Debe ingresar un número entero positivo'
    evens=0
    odds=0
    for digit in str(u):
        if int(digit)%2==0:
            evens+=1
        else:
            odds+=1
    return f'Dígitos pares: {evens}, Dígitos impares: {odds}'
print(evenAndOdds(156))

#2 Call your function factorial, it takes a whole number as a parameter and
#  it return a factorial of the number
numero=int(input('Put a number: '))
def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial
print(factorial(numero))

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
put=input('Put something: ')
def isEmpty(something):
    if put=="":
        return "Empty(you didn't put somenthing)."
    else:
        return "Not empty."
print(isEmpty(put))

#4 Write different functions which take lists. They should calculate_mean,
#  calculate_median, calculate_mode, calculate_range, calculate_variance,
#  calculate_std (standard deviation).
vals=[6,9,35,37,43,95,38,14]
def calMean(mean):
    return f'The mean value is {sum(vals)/len(vals)}'
print(calMean(vals))

def calMedian(median):
    vals.sort()
    l=len(vals)
    mitad=int(l/2)
    # Si la longitud es par, promediar elementos centrales
    if l%2==0:
        mediana=(vals[mitad - 1]+vals[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = vals[mitad]
    return f'The median value is {mediana}'
print(calMedian(vals))

def calMode(moda):
        from statistics import mode
        mod=mode(vals)
        return f'The mode is {mod}'    
print(calMode(vals))

def calRange(range):
    r=max(vals)-min(vals)
    return f'The range is {r}'
print(calRange(vals))

def calVariance(var):
    from statistics import variance
    v=variance(vals)
    return f'The variance is {v}'
print(calVariance(vals))

def calStd(stt):
    from statistics import stdev
    st=stdev(vals)
    return f'The Standard deviation is {st}'
print(calStd(vals))

                                              #Exercises: Level 3
#1 Write a function called is_prime, which checks if a number is prime.
def isPrime(p):
    if p<2:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
pop = int(input('Give a number: '))
if isPrime(pop):
    print(f'{pop} es un número primo.')
else:
    print(f'{pop} no es un número primo')

#2 Write a functions which checks if all items are unique in the list.
def uniqueData(lista):
    return len(lista)==len(set(lista))
print(uniqueData([1,2,3,5,6,4,2,2]))
print(uniqueData([1,5,4,2,]))

#3 Write a function which checks if all the items of the list are of the same data type.
def sameType(lista):
    return all(isinstance(i, type(lista[0])) for i in lista)
print(sameType([1,8,9]))
print(sameType([1,'nein',78]))
'''
#4 Write a function which check if provided variable is a valid python variable
import keyword
def validVar(nombre):
    return nombre.isidentifier() and not keyword.iskeyword(nombre)
print(validVar('mi_variable'))
print(validVar('2var'))
print(validVar('for'))

#5 Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
import COUNTRIES as lol
def mostSpokenLanguages():
    import COUNTRIES as lol
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

# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def paisesMasPoblados():
    dictPoblacion = {
    }
    for pais in datos:
        dictPoblacion[pais['name']] = pais['population']
    
    sortValuesPopulation = sorted(dictPoblacion.values(), reverse= True)
    sorfkeysPopulation = sorted(dictPoblacion, key= dictPoblacion.get, reverse=True)

    return sorfkeysPopulation[:10],sortValuesPopulation[:10]
print(paisesMasPoblados())

