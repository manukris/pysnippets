#python useful snippets

########################################################################################################################
# program to find anagram
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


print(anagram("abcd3", "3acdb")) # True

##########################################################################################################################
# normal program for anagrams My Logic

word1 = input("Enter a word1")
word2 = input("Enter a word2")
n1    = len(word1)
count = 0
for char in word1:
    if char in word2:
        count += 1
else:
    if count == n1:
        print("anagram")
    else:
        print("not a anagram")


################################################################################################

#This snippet can be used to check the memory usage of an object.

import sys

variable = "hello"
print(sys.getsizeof(variable)) #


#This method chunks a list into smaller lists of a specified size.















