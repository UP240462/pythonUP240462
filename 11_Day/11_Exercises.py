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
'''
#2 Call your function factorial, it takes a whole number as a parameter and
#  it return a factorial of the number
def factorial(number):
    return 

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not


#4 Write different functions which take lists. They should calculate_mean,
#  calculate_median, calculate_mode, calculate_range, calculate_variance,
#  calculate_std (standard deviation).