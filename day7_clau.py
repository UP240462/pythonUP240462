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
 