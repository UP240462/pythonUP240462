#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
finalPhrase = word1 + " " + word2 + " " + word3 + " " + word4
print(finalPhrase)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
w1 = "Codding"
w2 = "For"
w3 = "All"
finalWord = w1 + " " + w2 + " " + w3
print(finalWord)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print("The lenght is: ", len(company))

#6 Change all the characters to uppercase letters using upper() method.
wor1 = "Codign For All"
upper = wor1.upper()
print(upper)

#7 Change all the characters to lowercase letters using lower() method.
wor2 = "Codign For All"
lower = wor2.lower()
print(lower)

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
wor3 = "Codign For All"
capit = wor3.capitalize()
print(wor3.capitalize())
print(wor3.title())
print(wor3.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
wor4 = "Coding For All"
print(wor4[0:6])
print(wor4[7:15])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
wor5 = "Coding For All"
if "Coding" in wor5:
    print("Coding is in the string")

#11 Replace the word coding in the string 'Coding For All' to Python.
wor6 = "Coding For All"
print(wor6.replace("Coding", "Python"))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
wor7 = "Python for Everyone"
print(wor7.replace("Everyone", "All"))

#13 Split the string 'Coding For All' using space as the separator (split())
A = "Coding For All"
print(A.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
B = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(B.split(",")) 

#15 What is the character at index 0 in the string Coding For All.
A = "Coding For All"
print("The character in the possition 0 is: ", (A[0])) #C

#16 What is the last index of the string Coding For All.
A = "Coding For All"
print("The last character is: ", (A[-1])) #l

#17 What character is at index 10 in "Coding For All" string.
A = "Coding For All"
print("The character in the possition 10 is: ", (A[10])) #A

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
B = "Python For Everyone"
print(B[0] + B[7] + B[11]) #PFE

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
A = "Coding For All"
print(A[0] + A[7]+ A[11]) #CFA

#20 Use index to determine the position of the first occurrence of C in Coding For All.
A = "Coding For All"
print ("La primera aparición de C es en la posisicón: ", A.index("C")) #0

#21 Use index to determine the position of the first occurrence of F in Coding For All.
A = "Coding For All"
print ("F aparece en la posisicón: ", A.index("F")) #7

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
C = "Codging For All People"
print("L is in the last  possition of: ", C.rfind(("l"))) #20

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print("Because aparece por primera vez en la posisicón: ", sentence.index("because")) #31

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print("Because está como última posicion en: ", sentence.rindex("because")) #47

#25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.replace("because because because", "You cannot end a sentence with is a conjuction"))

#26 Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print("Because aparece por primera vez en la posisicón: ", sentence.find("because")) #31

#27 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.replace("You cannot end a sentence with ", "You cannot end a sentence with is a conjuction"))

#28 Does 'Coding For All' start with a substring Coding?
text = "Coding For All"
text2 = "Coding"
print(text.startswith(text2))

#29 Does 'Coding For All' end with a substring coding?
text = "Coding For All"
text2 = "coding"
print(text.endswith(text2))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = "   Coding For All      "
print(text.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython | thirty_days_of_python
F1 = "30DaysOfPython"
F2 = "thirty_days_of_python"
print(F1.isidentifier()) #False
print(F2.isidentifier()) #True

#32 The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space string.
Librerías = ('Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon')
print(" # ".join(Librerías))

#33 Use the new line escape sequence to separate the following sentences.
# 'I am enjoying this challenge. \nI just wonder what is next.'
frase = "I am enjoying this challenge\nI just wonder what is next."
print(frase)

#34 Use a tab escape sequence to write the following lines.
# 'Name      Age     Country      City'
frase2 = "Name\tAge\tCountry\tCity"
print(frase2) 

#35 Use the string formating method to display the following:
# 'radius = 10.0, area = 3.14159'
radio = 10.0
area = 3.14159 * radio ** 2
print("El área del círculo con un radio de = {} es de = {} metros cuadrados. ".format(radio, area))

#36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {}".format(8 / 6))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))

#REVISADO
print("Revisado")