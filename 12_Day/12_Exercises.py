                                        #Exercises: Level 1
#1 Write a function which generates a six digit/character random_user_id.
from modulos import randomUserID
print(randomUserID())

#2 Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of 
# IDs which are supposed to be generated.
from modulos import userByUser
print(userByUser())

#3 Write a function named rgb_color_gen. It will generate rgb colors
#  (3 values ranging from 0 to 255 each).
from modulos import rgbColorGen
print(rgbColorGen())

                                         #Exercises: Level 2
#1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an
#  array (six hexadecimal numbers written after #. Hexadecimal numeral system
#  is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
#  Check the task 6 for output examples).
from modulos import hexaColors
print(hexaColors(3))

#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
from modulos import listOfRgbColors
print(listOfRgbColors(3))

#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
from modulos import generateColors
print(generateColors('hexa',5))
print(generateColors('rgb',3))

                                        #Exercises: Level 3
#1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
from modulos import shuffleList
lola=[90,'winter',78,3,'chocolate']
print('La lista mezclada:',shuffleList(lola))

#2 Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
from modulos import uniqueRandomNumbers
print(uniqueRandomNumbers())

print("revisado")