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

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



