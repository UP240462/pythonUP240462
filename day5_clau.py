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
itCompanies.insert(2, "BOZ IT DEVELOPMENT")
print(itCompanies)
