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
#1 Join A and B
set1 = {'A'}
set2 = {'B'}
set1.update(set2)

#2 Find A intersection B


#3 Is A subset of B


#4 Are A and B disjoint sets


#5 Join A with B and B with A


#6 What is the symmetric difference between A and B


#7 Delete the sets completely