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
        for word in word_list:
        
        # Loop until you reach the end of the list, or the value at the
        # current position is equal to the key
            while current_line_position < len(line) and dictionary_word_list[current_line_position] != word.upper():

            # Advance to the next item in the list
                current_line_position += 1

                if current_line_position < len(line):
                    print("The word is at position", current_line_position)
                else:
                    print(f"The word was not in the list {word_list[current_line_position]}.")
            


main()
        



