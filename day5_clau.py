#1 Declare and empty list
listA1 = []
print(listA1)

#2 Declare a list with more than 5 items
listA2 = [1, 9, 78, 6, 36]
print(listA2)

#3 Find the length of your list
print("La lista 2 tiene", len(listA2), " elementos")

#4 Get the first item, the middle item and the last item of the list
print("El primer número de la lista 2 es: ", listA2[0])
print("El número del medio de la lista 2 es: ", listA2[2])
print("El último número de la lista 2 es: ", listA2[-1])

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixedDataTypes = ["Claudia, 18, 1.60, soltera, Santa Fe #259"]
print(mixedDataTypes)

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
itCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list using print()
print(itCompanies)

#8 Print the number of companies in the list
print("El total de empresas de la lista es: ", len(itCompanies))

#9 Print the first, middle and last company
print("Primera empresa: ", itCompanies[0])
print("Empresa del medio: ",itCompanies[3])
print("La última empresa es: ", itCompanies[6])

#10 Print the list after modifying one of the companies.
itCompanies [0] = "Netflix"
print(itCompanies)

#11 Add an IT company to it_companies
itCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
itCompanies.insert(2, "Boz It Development")
print(itCompanies)

#12 Insert an IT company in the middle of the companies list.
itCompanies.insert(4, "Red Bull")
print(itCompanies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
itCompanies[5]  = itCompanies[5].upper()
print(itCompanies)

#14 Join the it_companies with a string '#;'
print("#;".join(itCompanies))

#15 Check if a certain company exists in the it_companies list.
if "Apple" in itCompanies:
    print("Apple está en la lista")

#16 Sort the list using sort() method
itCompanies.sort()
print(itCompanies)

#17 Reverse the list in descending order using reverse() method
itCompanies.reverse()
print(itCompanies)

#18 Slice out the first 3 companies from the list
print(itCompanies[3:5])

#19 Slice out the last 3 companies from the list
print(itCompanies[3:6])

#20 Slice out the middle IT company or companies from the list
print(itCompanies[3:4])

#21 Remove the first IT company from the list
itCompanies.pop(0)
print(itCompanies)

#22 Remove the middle IT company or companies from the list
itCompanies.remove("Apple")
print(itCompanies)

#23 Remove the last IT company from the list
itCompanies.pop()

#24 Remove all IT companies from the list
itCompanies.clear()
print(itCompanies)

#25 Destroy the IT companies list
del itCompanies

#26 Join the following lists:
frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node','Express', 'MongoDB']
fullList = frontEnd + backEnd
print(fullList)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
fullListCOPY = fullList.copy()
fullListCOPY.insert(5, "Python")
fullListCOPY.insert(6, "SQL")
print(fullListCOPY)

#28 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print("La edad máxima es: ", ages[9])
print("La edad mínima es: ", ages[0])
#Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[9])
print(ages)
#Find the median age (one middle item or two middle items divided by two)
mediana = (ages[4] + ages[5]) / 2
print("La mediana es: ", mediana)
#Find the average age (sum of all items divided by their number )
promedio = sum(ages) / len(ages)
print("El promedio de edad es: ", promedio)
#Find the range of the ages (max minus min)
rango = ages[9] - ages[0]
print("El rango de edades es: ", rango)
#Compare the value of (min - average) and (max - average), use abs() method
comparation = (ages[0] - promedio) - (ages[9] - promedio)
print("La comparación es: ", comparation)


#29 Find the middle country(ies) in the countries list
import paises as paises
print(len(paises.countries)) 
n = (len(paises.countries))/2
print(n)
int(n)
print(paises.countries[int(n-1)]+" , "+paises.countries[int(n)])

#30 Divide the countries list into two equal lists if it is even if not one more country for the first half.
P1Lista = paises.countries[0:95]
P2Lista = paises.countries[96:192]
print("Lista 1: ", P1Lista)
print("Lista 2: ", P2Lista)

#31 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
paises.countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
p1, p2, p3, *scandic = paises.countries
print(*scandic) 
