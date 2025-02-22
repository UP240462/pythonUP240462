
# Variables in Python

first_name = 'Claudia'
last_name = 'Arroyo'
country = 'Germany'
city = 'Bavaria'
age = 22
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Claudia', 
    'lastname':'Arroyo', 
    'country':'Germany',
    'city':'Bavaria'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Claudia', 'Arroyo', 'Bavaria', 22, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

##Area del circulo
radio=int(input('Ingresa el radio del circulo: '))
print(type(radio))
pi=3.14159
areaOfCircle=pi*radio**2
circumOfCircle=2*pi*radio
print("The area of the circle is", areaOfCircle)
print('The circumference of the circle is', circumOfCircle)

##Variable
firstName=input('Enter your first name: ')
lastName=input('Enter your last name: ')
country=input('What is your country: ')
age=input('Your age: ')
print('your name is: '+firstName+' '+lastName)
print('You are from: '+ country)
print('Your are: '+ age + ' years old')