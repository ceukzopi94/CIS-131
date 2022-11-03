"""
Christian Urbanski
CIS 131
10/24/2022

This program implements a relusive fibonacci function along with a funciton call counter to demonstrates
"""

#put constants here
fib_called_count = 0 #counter for how many times fibonacco(n) function is called

def main(): 
    #put code here
    display_fib(10)
    display_fib(20)
    display_fib(30)
    

def fibonacci(n):
    """Recursive function that calculates and returns the total value."""
    global fib_called_count
    fib_called_count += 1 #increment counter after each call.

    if n in (0, 1): #base case
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def display_fib(num):
    """Function to print out fibonacci and amount of times the function got called."""
    global fib_called_count
    fib_called_count = 0 #reset counter to 0.

    print(f'Fibonacci({num}) = {fibonacci(num)}')
    print(f'Times fibonacci(n) function called: {fib_called_count}\n')


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
