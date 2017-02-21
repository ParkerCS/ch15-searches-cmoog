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

alice_chapter1 = open("AliceInWonderLand200.txt", "r")
chapter_1_list = []
for line in alice_chapter1:
    line_in_file = split_line(line)
    for j in range(len(line_in_file)):
        for k in range(len(dictionary_list)):
            if line_in_file[j].upper() == dictionary_list[k]:
                break
            elif k == len(dictionary_list) - 1:
                print(line_in_file[j], "was not found.")


