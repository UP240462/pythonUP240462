                                            #Exercises: Level 1
#Get user input using input(“Enter your age: ”). 
#If user is 18 or older, give feedback: You are old enough to drive. 
#If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input('Put your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print('You cannot drive, wait for the missing years')

#Compare the values of my_age and your_age using if … else. 
#Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 
#'years' for bigger differences, and a custom text if my_age = your_age. Output:
me = 18
you = int(input('Give me your age: '))
if you > me:
    diff = you - me
    print('You are older than me for {} years.'.format(diff))
    if me > you:
        diff2 = me - you
        print('I am {} older than you.'.format(diff2))
else:
    print('We are the same age.')

#Get two numbers from the user using input prompt. 
#If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
#else a is equal to b. Output:
a = input('Type one number: ')
b = input('Type one number again: ')
if a < b:
    print('{} is smaller than {}'.format(b,a))
elif a > b:
    print('{} is grater than {}'.format(b,a))
else:
    print('Are the same numbers.')

                                              #Exercises: Level 2
#Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

grade = float(input('Your grade: '))
if grade>=80 and grade<=100:
    print('A')
elif grade>=70 and grade<=89:
    print('B')
elif grade>=60 and grade<=69:
    print('C')
elif grade>=50 and grade<=59:
    print('D')
elif grade>=0 and grade<=49:
    print('F')

#Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. 
#December, January or February, the season is Winter. 
#March, April or May, the season is Spring June, July or August, the season is Summer
seas = input('Give me a month: ')
yesSeas = seas.capitalize()
aut = ('September','Octover','November')
wint = ('December','January','February')
spr = ('March','April','May')
summ = ('June','July','August')
if yesSeas in aut:
    print('The season is Autumn.')
elif yesSeas in wint:
    print('The season is Winter.')
elif yesSeas in spr:
    print('The season is Spring.')
elif yesSeas in summ:
    print('The season is Summer.')

#The following list contains some fruits:
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
#If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
newFruit = input('Add a fruit: ')
if newFruit not in fruits:
    fruits.append(newFruit)
    print(fruits)
else:
    print('The fruit already exists.')


                                            #Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
profile ={
    'first_name': 'Claudia',
    'last_name': 'Arroyo',
    'age': 18,
    'country': 'Georgia',
    'is_married': True,
    'skills': ['JavaScript', 'German', 'Horse Riding', 'Python', 'Painting'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#1 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in profile:
    print(profile['skills']
          [len(profile['skills'])//2])

#2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill 
#and print out the result.
if 'skills' in profile:
    if 'Python' in profile['skills']:
        print['skills']

#3  If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in profile:
    sk = profile['skills']
    if 'JavaScript'in sk or 'React' in sk:
        print('He is a front end developer')
    elif 'Node'in sk or 'Python' in sk or 'MongoDB'in sk:
        print('He is a backend developer')
    elif 'Node'in sk or 'React'in sk or 'MongoDB'in sk:
        print('He is a fullstack developer')
    else:
        print('unknown title')

#4 If the person is married and if he lives in Finland, print the information in the following format:
#Asabeneh Yetayeh lives in Finland. He is married.
if 'is_married' in profile and 'country' in profile:
    if profile['is_married'] == True and profile['country']== 'Finland':
        print(f'{profile["first_name"]} {profile["last_name"]} lives in Finland. She is married.')
    else:
        print(f'{profile["first_name"]} {profile["last_name"]} lives in {profile["country"]}.She is not married.')