'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

dictionary_list = []

dictionary = open("dictionary.txt", "r")
for line in dictionary:
    dictionary_list.append(line.strip())

top_length = 0
longest_words = []
for i in range(len(dictionary_list)):
    if len(dictionary_list[i]) > top_length:
        longest_words = []
        top_length = len(dictionary_list[i])
        longest_words.append(dictionary_list[i])
    elif len(dictionary_list[i]) == top_length:
        longest_words.append(dictionary_list[i])
print(longest_words)

#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

import re
def split_line(line):
    # This function takes in a line of text and returns a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
alice_list = []
file = open("AliceInWonderLand.txt", "r")
for line in file:
    alice_list.append(split_line(line))
print("There are", len(alice_list), "words in Alice and Wonder Land, ", end="")

index = 0
for j in range(len(alice_list)):
    index += len(alice_list[j])
average_length = index / len(alice_list)
print("with an average word length of", average_length, "letters.")


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



