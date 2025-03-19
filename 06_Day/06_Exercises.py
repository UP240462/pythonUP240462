#1 Create an empty tuple
emptyTuple = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
TupleFam = ("Emilio", "Ana", "Luisa", "Jaun pablo", "Galea")

#3 Join two tuples
TupleBrothers = ("Emilio", "Juan Pablo")
TupleSisters = ("Ana", "Luisa", "Galea")
Siblings = TupleBrothers + TupleSisters
print(Siblings)

#4 Create a tuple with single value
print("I have {} siblings".format(len(Siblings)))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
familyMembers = Siblings + ("Claudia", "Ramón")
print(familyMembers)

#6 Unpack siblings and parents from family_members
Br1, Br2, Sis1, Sis2, Sis3, Mom, Dad = familyMembers
print(Sis1, Sis2, Sis3)
print(Mom, Dad)

#7 Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
animalsPr = ("Chesse", "Eggs", "Milk")
fruits = ("Grapes", "Banana", "Orange", "Sandía")
vegetables = ("Tomato", "Lettuce", "Carrot", "Broccoli")
foodStuffTp = animalsPr + fruits + vegetables
print(foodStuffTp)

#8 Change the about food_stuff_tp tuple to a food_stuff_lt list
foodStuffLt = list(foodStuffTp)
print(foodStuffLt)

#9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = foodStuffTp[5]
print(middle)

#10 Slice out the first three items and the last three items from food_staff_lt list
firstThree = foodStuffTp[0:3]
lastThree = foodStuffTp[-3:-1]
print(firstThree)
print(lastThree)

#11 Delete the food_staff_tp tuple completely
del foodStuffTp

#12 Check if an item exists in tuple:
if "Sandía" in foodStuffLt:
    print("Yes, 'Sandía' is in the fruits tuple")

#13 Check if 'Estonia' is a nordic country
#14 Check if 'Iceland' is a nordic country
nordicCountries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
if "Iceland" in nordicCountries:
    print("Iceland is a nordic country")

if "Estonia" in nordicCountries:

    print("Estonia is a nordic country")
else:
    print("Estonia is not a nordic country")

    #REVISADO
print("Revisado")