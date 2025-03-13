#1 Create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog = {'Bruno','Black','Australian Shepherd','4 Legs','5 Age'}

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary
student = {'firstName': 'Miran',
           'lastName':'Sadoglu',
           'Gender':'Male',
           'Age':18,
           'maritalStatus:':'Married',
           'Skills':['Speak German and English'],
           'Country:':'Turkey',
           'City':'Capadoccia',
           'Adress':'Not yet'}

#4 Get the length of the student 
print('The lenght of the Dictionary is:', len(student))

#5 Get the value of skills and check the data type, it should be a list
print('The values of SKILLS are:', student['Skills'])

#6 Modify the skills values by adding one or two skills
student['Skills'] = 'Python'',''Administration','Speak German and English'
print(student)

#7 Get the dictionary keys as a list
claves = (student.keys())
print('The keys are:', claves)

#8 Get the dictionary values as a list
val = (student.values())
print('The values are:', val)

#9 Change the dictionary to a list of tuples using items() method
print(student.items())

#10 Delete one of the items in the dictionary
del(student['Age'])
print(student)

#11 Delete one of the dictionaries
del(student)