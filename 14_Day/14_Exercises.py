import functools
from functools import reduce

                                    #Exercises: Level 1
#1 Explain the difference between map, filter, and reduce.
print('Map: toma una función y un iterable como parámetros.')
print('Filtler')

#2 Explain the difference between higher order function, closure and decorator


#3 Define a call function before map, filter or reduce, see examples.


#4 Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def printCountry(country):
    for c in countries:
        print(c)
    return""
print(printCountry(countries))

#5 Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def printName(name):
    for n in names:
        print(n)
    return ""
print(printName(names))

#6 Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def printNumber(number):
    for n in numbers:
        print(n)
    return ""
print(printNumber(numbers))

                                         #Exercises level: 2

#1 Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def toUppCase(c):
    return c.upper()
finalC=list(map(toUppCase, countries))
print(finalC)

#2 Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(n):
    return n**2
finalN=list(map(square, numbers))
print(finalN)

#3 Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def nUpperC(name):
    return name.upper()
finalN=list(map(nUpperC, names))
print(finalN)

#4 Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def filtLand(pais):
    if 'land' in pais:
        return True
    return False
print(list(filter(filtLand, countries)))

#5 Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixCarac(p):
    if len(p)==6:
        return True
    return False
print(list(filter(sixCarac, countries)))

#6 Use filter to filter out countries containing six letters and more in the country list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixOrMoreCarac(p):
    if len(p)>=6:
        return True
    return False
print(list(filter(sixOrMoreCarac, countries)))

#7 Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def startE(m):
    if m[0=='E']:
        return True
    return False
print(list(filter(startE, countries)))

#8 Use filter to filter out only digits from the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def onlyDid(d):
    if type(d)==int:
        return True
    return False
print(list(filter(onlyDid, numbers)))

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = reduce(
    lambda acc, num: acc + num,  # Suma los elementos
    filter(
        lambda x: x > 10,  # Filtra los números mayores a 10
        map(lambda x: x * 2, numeros)  # Multiplica cada número por 2
    ),
    0  # Valor inicial de la suma
)

print(resultado)  # Salida: 54

#9 Declare a function called get_string_lists which takes a list as a parameter
#  and then returns a list containing only string items.
pera=['Estonia', 1, 'Finland', 2, 'Sweden', 3, 'Denmark', 4, 'Norway', 5, 'Iceland']
def getStringLists(lista):
    def isString(lista):
        if type(lista) == str:
            return True
        return False
    return (list(filter(isString, lista)))
print(list(getStringLists(pera)))

#10 Use reduce to sum all the numbers in the numbers list.
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    

#11 Use reduce to concatenate all the countries and to produce this sentence:
#  Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def concatCountries(countries):
    return reduce(lambda acc, country: acc + ', ' + country, countries)
result = concatCountries(countries)

#12 Declare a function called categorize_countries that returns a list of countries with some common
#  pattern (you can find the countries list in this repository as
#  countries.js(eg 'land', 'ia', 'island', 'stan')).
from paises import countries  
def categorizeCountries(patterns):
    categorized = {}
    for pattern in patterns:
        categorized[pattern] = [country for country in countries if pattern in country]
    return categorized
patterns = ['land', 'ia', 'island', 'stan']
result = categorizeCountries(patterns)
print(result)

#13 Create a function returning a dictionary, where keys stand for starting letters of countries
#  and values are the number of country names starting with that letter.
from paises import countries
def countI():
    initialCount = {}
    for country in countries:
        initial = country[0].upper()
        if initial not in initialCount:
            initialCount[initial] = 1
        else:
            initialCount[initial] += 1
    return initialCount
initialCount = countI()
print(initialCount)

#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from
#  the countries.js list in the data folder.
def FirssTen():
    return countries[:10]
FirstTen = FirssTen()
print(FirstTen)

#15  a get_last_ten_countries function that returns the last ten countries in the countries list.
def LastC():
    return countries[-10:]
LastTen = LastC()
print(LastTen)

                                            #Exercises level: 3
#1 Sort countries by name, by capital, by population.
import paises as LOL  
def obtenerNombre(pais):
    return pais["name"]
def obtenerCapital(pais):
    return pais["capital"]
def obtenerPoblacion(pais):
    return pais["population"]
def ordenarPorNombre(paises):
    return sorted(paises, key=obtenerNombre)
def ordenarPorCapital(paises):
    return sorted(paises, key=obtenerCapital)
def ordenarPorPoblacion(paises, reverse=False):
    return sorted(paises, key=obtenerPoblacion, reverse=reverse)
paisesLista = LOL.countries  
ordenadoPorNombre = ordenarPorNombre(paisesLista)
print("\nOrdenado por nombre:")
for pais in ordenadoPorNombre:
    print(pais["name"])
ordenadoPorCapital = ordenarPorCapital(paisesLista)
print("\nOrdenado por capital:")
for pais in ordenadoPorCapital:
    print(pais["capital"])
ordenadoPorPoblacion = ordenarPorPoblacion(paisesLista, reverse=True)
print("\nOrdenado por población (de mayor a menor):")
for pais in ordenadoPorPoblacion:
    print(f"{pais['name']} - {pais['population']}")

#2 Sort out the ten most spoken languages by location.
from collections import Counter
import paises as LOL
def contarTop10Idiomas():
    idiomas = []
    for pais in LOL.countries:  
        if "languages" in pais:  
            idiomas.extend(pais["languages"]) 
    top10Idiomas = Counter(idiomas).most_common(10)
    return top10Idiomas
def mostrarTop10Idiomas():
    top10Idiomas = contarTop10Idiomas()
    print("Los 10 idiomas más hablados globalmente son:",top10Idiomas)
    for idioma, count in top10Idiomas:
        print(f"{idioma}: {count}")
mostrarTop10Idiomas()

#3 Sort out the ten most populated countries.
def clasificarPaisesMasPoblados():
    paisesOrdenados = sorted(LOL.countries, key=lambda pais: pais["population"], reverse=True)
    return paisesOrdenados[:10]
def mostrarTop10PaisesMasPoblados():
    top10Paises = clasificarPaisesMasPoblados()
    print("Los 10 países más poblados son:")
    for pais in top10Paises:
        print(f"{pais['name']}: {pais['population']}")
mostrarTop10PaisesMasPoblados()