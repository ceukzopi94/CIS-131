"""
Christian Urbanski
CIS 131
10/26/2022

"""

#put constants here


def main(): 
    #put code here
    word_to_test = 'rader'


    is_palindrome = test_palindrome(word_to_test, 0, len(word_to_test) - 1)

    print(f'"{word_to_test}" is a palindrome: {is_palindrome}')
    
def test_palindrome(word=str, letter1_pos=0, letter2_pos = 0):
    """Reclusive Function to test if word is a palindrome or not."""

    print(f'word[letter1_pos] == {word[letter1_pos]}')
    print(f'letter1_pos: {letter1_pos}')
    print(f'word[letter2_pos] == {word[letter2_pos]}')
    print(f'letter2_pos: {letter2_pos}\n')

    if word[letter1_pos] == ' ':
        print('letter1_pos: space encountered.')
        test_palindrome(word, letter1_pos + 1, letter2_pos)
    
    if word[letter2_pos] == ' ':
        print('letter2_pos: space encountered.')

        test_palindrome(word, letter1_pos, letter2_pos - 1)

    if word[letter1_pos] != word[letter2_pos]:
        print('should return false.')
        return False

    if letter2_pos >= letter1_pos:
        test_palindrome(word, letter1_pos + 1, letter2_pos - 1)

    return True

#---------------------------------------------------------------------------------


def get_integer(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:            
            newValue = int(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')

def get_float(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:
            newValue = float(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')
    
def get_string(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        newValue = input()
        if newValue and newValue.strip():
            return newValue
        else:
            print('Error: no data entered')
            
def get_yes_or_no(message, prompt="none"):
    while True:
        new_value = get_string(message, prompt)
        new_value = new_value.lower()
        if new_value == "y" or new_value == "yes":
            return True
        if new_value == "n" or new_value == "no":
            return False
        print('Error: invalid value entered') 

def display_prompt(message, prompt):
        print(message, end="")
        if prompt != "none":
            print ("\n" + prompt + " ", end="")

"""
loop that creates a grid of rows and columns for things to be placed in. 
    for row in range(1, MAX_ROWS + 1):
        for col in range(1, MAX_COLS + 1):
"""

#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
