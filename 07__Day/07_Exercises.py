#Exercises: Level 1
#1 Find the length of the set it_companies
itCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(itCompanies))

#2 Add 'Twitter' to it_companies
itCompanies.add("Twitter")
print(itCompanies)

#3 Insert multiple IT companies at once to the set it_companies
itCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
itCompanies.update(["Instagran", "TikTok", "Snapchat"])
print(itCompanies)

#4 Remove one of the companies from the set it_companies
itCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(itCompanies.pop())

#5 What is the difference between remove and discard
#Si usando remove() el item no se encuentra en el set, arrojará error
#En cambio discard no arrojará nada

#Exercises: Level 2
#Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)

#Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.intersection(B)
print(A)    

#Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.issubset(B)

#Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))

#Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union1 = A.union(B)
union2 = B.union(A)
print("A with B: ", union1)
print("B with A: ", union2)

#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
(print(A.symmetric_difference(B)))

#Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A
del B

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
setAge = set(age)
print(len(age))
print(len(setAge))
if len(age) > len(setAge):
    print("La lista mayor es: ", age)
if len(age) < len(setAge):
    print("El set mayor es: ", setAge)

#Explain the difference between the following data types: string, list, tuple and set
print("Un String es una cadena de caracteres")
print("Una lista es una estructura de datos que almacena elementos de manera ordnada")
print("Un tuple es lo mismo que une lista pero no se puede modificar")
print("Un set es una colección de elementos que; no se repiten y no tienen un orden y los sets"" " 
"son inmutables")

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
word = "I am a teacher and I love to inspire and teach people"
totalWords = word.split()
print("Las palabras unicas son: ", len(totalWords))
print("Las palabras unicas son; ", totalWords)