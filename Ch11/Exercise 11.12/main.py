"""
Christian Urbanski
CIS 131
10/25/2022

Program demonstrates the Tower of Hanoi game by solving it in a reclusive function.
"""

times_moved = 0

def main(): 
    #put code here
    disks = get_integer('How many disks do you wish to start with?')

    move_disks(disks, 1, 3, 2)
    

def move_disks(disks, starting_peg, destination_peg, temp_peg):
    """Recursive function to move the disks"""
    global times_moved

    if disks >= 1:

        #call that sets the final destination of the peg to be moved
        #goes through how many disks needs to be moved 
        #and sets destination peg and temp peg respectivly
        move_disks(disks - 1, starting_peg, temp_peg, destination_peg) 

        times_moved += 1
        print(f'Move {times_moved}: {starting_peg} --> {destination_peg}')

        #call to move the disk in the temp peg to the propper spot
        move_disks(disks - 1, temp_peg, destination_peg, starting_peg)


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


#------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
