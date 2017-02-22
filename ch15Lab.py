'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

dictionary = open("dictionary.txt", "r")
dictionary_list = []
for line in dictionary:
    dictionary_list.append(line.strip())
dictionary.close()

print("---Linear Search---")

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
'''
alice_chapter1 = open("AliceInWonderLand200.txt", "r")

for line in alice_chapter1:
    line_in_file = split_line(line)
    for j in range(len(line_in_file)):
        for k in range(len(dictionary_list)):
            if line_in_file[j].upper() == dictionary_list[k]:
                break
            elif k == len(dictionary_list) - 1:
                print(line_in_file[j], "was not found.")
alice_chapter1.close()
'''
print("--- Binary Search ---")
def binary_search(input_key, dictionary_list):
    key = input_key.upper()
    lower_bound = 0
    upper_bound = len(dictionary_list) - 1
    found = False
    # loop until we find item or the bounds meet
    while lower_bound <= upper_bound and not found:
        # find the middle
        middle_position = (lower_bound + upper_bound) // 2
        # figure out if we need to move up or down
        if dictionary_list[middle_position] < key:
            lower_bound = middle_position + 1
        elif dictionary_list[middle_position] > key:
            upper_bound = middle_position - 1
        else:
            found = True
    return found

alice_chapter1 = open("AliceInWonderLand200.txt", "r")
for line in alice_chapter1:
    line_in_file = split_line(line)
    for j in range(len(line_in_file)):
        found = binary_search(line_in_file[j], dictionary_list)
        if not found:
            print(line_in_file[j])



