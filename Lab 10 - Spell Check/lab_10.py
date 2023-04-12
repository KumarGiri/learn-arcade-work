import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    dictionary = open("Lab 10 - Spell Check\dictionary.txt")
    
    dictionary_word_list = []

    for word in dictionary:
        word = word.strip()
        dictionary_word_list.append(word)
    dictionary.close()

# Linear Search
    print("--- Linear Search ---")

    Alice = open("Lab 10 - Spell Check\AliceInWonderLand200.txt")
    current_line_position = 0

 

    for line in Alice:
        line =line.strip()
        word_list = split_line(line)
        current_line_position +=1
        for word in word_list:
            current_d_word_position = 0
            while current_d_word_position < len(dictionary_word_list) and dictionary_word_list[current_d_word_position]!=word.upper():
                current_d_word_position += 1
            
            if current_d_word_position < len(dictionary_word_list):
                continue
            else:
                print(f"line {current_line_position} Possible error word: {word}.")
            


main()
        



