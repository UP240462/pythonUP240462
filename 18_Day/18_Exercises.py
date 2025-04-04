                                          #Exercises: Level 1
#1 What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love.' \
' I love Python if you do not love something which can give you all the capabilities to develop' \
' an application what else can you love.'
import re
from collections import Counter
words = re.findall(r'\b\w+\b', paragraph.lower())
wordCounts = Counter(words)
mostFrequentWord = wordCounts.most_common(1)[0]

print(f"The most frequent word is '{mostFrequentWord[0]}' with {mostFrequentWord[1]} occurrences.")

#2 The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative
#  direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole
#  text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12)

pointsInt = [int(point) for point in points]
furthestDistance = max(pointsInt) - min(pointsInt)

print(f"The distance between the two furthest particles is {furthestDistance}.")
