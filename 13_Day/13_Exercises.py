#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtler=[n for n in numbers if n<=0]
print(filtler)

#2 Flatten the following list of lists of lists to a one dimensional list:
listOfLists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattList=[item for sublist in listOfLists for inner_list in sublist for item in inner_list]
print(flattList)

#3 Using list comprehension create the following list of tuples:
#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]
listTuples=[(x, 1, *[x**i for i in range(1, 7)]) for x in range(11)]
print(listTuples)

#4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
fCount=[item for sublist in countries for inner_list in sublist for item in inner_list]
print(fCount)

#5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lstOfDics=[{'country': country, 'city': capital} for country_capital in countries for country, capital in country_capital]
print(lstOfDics)

#6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatNames = [' '.join(name) for sublist in names for name in sublist]
print(concatNames)

#7 Write a lambda function which can solve a slope or y-intercept of linear functions.
# Lambda function to calculate the slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate the y-intercept
y_intercept = lambda x1, y1, m: y1 - m * x1

# Example usage
x1, y1 = 1, 4
x2, y2 = 3, 6

m = slope(x1, y1, x2, y2)  # Calculate slope
b = y_intercept(x1, y1, m)  # Calculate y-intercept

print(f"Slope (m): {m}")
print(f"Y-Intercept (b): {b}")