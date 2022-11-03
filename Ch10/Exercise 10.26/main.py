"""
Christian Urbanski
CIS 131
10/17/2022

This programs shows effective inheritance hierarchies with concrete and abstract classes
"""
from employee import Employee
from salariedemployee import SalariedEmployee
from hourlyemployee import HourlyEmployee

#put constants here

def main(): 

    try: 
        #try and create an object of an abstract class.
        employee = Employee('Bob', 'Smith', '654-89-7985')
    except TypeError:
        #this shows that you cannot create an object of an abstract class.
        print('\nCannot create objects of abstract class.')

    #creats objects of employee sub classes
    salary_employee = SalariedEmployee('Justin', 'Case', '478-14-3486', 1478)
    hourly_employee = HourlyEmployee('Bob', 'Harper', '788-74-1684', 48, 32.5)

    print('\n***Displayed by individual print statements***\n')

    display_employee_data(salary_employee)
    display_employee_data(hourly_employee)

    employees = [salary_employee, hourly_employee] #list of employees

    print('\n***Displayed by polymorphic loop calls***\n')

    for employee in employees: #loops through list of employees to display their data
        display_employee_data(employee)

def display_employee_data(employee):
    """Function to display the employee attributes and earnings."""
    print(employee)
    print(f'Total Earnings: ${employee.earnings():,.2f}\n')
    
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
