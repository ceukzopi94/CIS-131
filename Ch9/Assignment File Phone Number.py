"""
Christian Urbanski
CIS 131
09/06/2022

takes phone number and converts numbers to corresponding letters
does this to create every possible combination of letters with numbers
"""

#put constants here
PHONE_LETTERS = {2:['A', 'B', 'C'], 
                3:['D', 'E', 'F'], 
                4:['G', 'H', 'I'], 
                5:['J', 'K', 'L'], 
                6:['M', 'N', 'O'], 
                7:['P', 'R', 'S'], 
                8:['T', 'U', 'V'], 
                9:['W', 'X', 'Y']}


def main(): 
    #put code here
    num_to_check = '7382273'
    num_to_word = [0] * len(num_to_check)

    word_count = 0 #counts how many words have been created

    with open('phone_words.txt', mode='w') as words:
        for first_letter in PHONE_LETTERS[int(num_to_check[0])]:
            num_to_word[0] = first_letter

            for second_letter in PHONE_LETTERS[int(num_to_check[1])]:
                num_to_word[1] = second_letter

                for third_letter in PHONE_LETTERS[int(num_to_check[2])]:
                    num_to_word[2] = third_letter

                    for forth_letter in PHONE_LETTERS[int(num_to_check[3])]:
                        num_to_word[3] = forth_letter

                        for fifth_letter in PHONE_LETTERS[int(num_to_check[4])]:
                            num_to_word[4] = fifth_letter

                            for sixth_letter in PHONE_LETTERS[int(num_to_check[5])]:
                                num_to_word[5] = sixth_letter

                                for seventh_letter in PHONE_LETTERS[int(num_to_check[6])]:
                                    num_to_word[6] = seventh_letter
                                    word_count += 1

                                    data_to_store = generate_word(num_to_word, word_count)
                                    store_data_to_file(data_to_store, words)

                                print('') # formats output to go to next line every 3 words for readability


def generate_word(lst, count):
    word = ''
    
    for letter in lst:
        word += letter

    data_to_store = f'{count:>5}: {word:>8}'
    print(data_to_store, end = '   ')

    return data_to_store


def store_data_to_file(data_to_store, words):
    print(data_to_store, file = words)


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
