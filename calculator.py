# Nathan Reid
# Nov. 12th, 2022
# Creating a calculator


import math

# calculator operation functions
def division(num_1, num_2):
    '''Create a mathmetical operation that allow one number
    to divide into another number.
    '''
    div = num_1 / num_2
    return div
    

def addition(num_1, num_2):
    '''Create a mathmetical operation that combines multiple
    numbers values to sum a new value.
    '''
    add = num_1 + num_2
    return add


def subtraction(num_1, num_2):
    '''Create a mathmetical operation that allow a number's value to be decreased
    by another number's value.
    '''
    sub = num_1 - num_2
    return sub
    

def multiplication(num_1, num_2):
    '''Create a new number by multipling the values of 
    two numbers.
    '''
    multi = num_1 * num_2
    return multi


def pi(num_1):
    '''Create a new number by times a number by pi.
    '''
    pi_number = math.pi * num_1
    return pi_number


def expo(num_1, exponent=2):
    '''Find the exponent (of 2) of a given number.'''
    new_value = pow(num_1, exponent)
    return new_value


def cube(num_1):
    '''Find the cube root of a given number.'''
    three = num_1 ** 3
    return three


def decimal(num_1):
    '''Convert a number or integar into a float or decimal.'''
    new_dec = float(num_1)
    return new_dec


def clear(cal_sum):
    '''Delete the current numerical total. Reset the calculator.'''
    erase = cal_sum - cal_sum
    return erase


# flag for while loop
On = True

# use list to not display second number for operations that don't need it
second_nums = [ 'add', 'subtract', 'multiply', 'divide']

# turn on the calculator
while On:

    # calculator current total at the start of operations
    cal_sum = 0

    # prompt user to select the numbers they want to use with the calculator operators
    while True:
        # catch error if user enters in string
        try:
            num_1 = int(input("Select first number: "))
            # float(num_1) if '.' in num_1 else int(num_1)  - NOTE - trying to get input to take int and float
            break
        except ValueError:
            print("\nOnly enter in a whole numbers not decimals.")

    # ask user what operation they want to use with the numbers
    cal_action = input("What calculation operation you want to use? ")

    # check for correct operation selection
    if cal_action in second_nums:
        # catch error if user enters in string
        while True: 
            try:
                num_2 = int(input("Select second number: "))
                # float(num_2) if '.' in num_2 else int(num_2) -  - NOTE - trying to get input to take int and float
                break
            except ValueError:
                print("\nOnly enter in a whole numbers not decimals.")
    else:
        print("Please enter in a operation not a number. Start over.\n")

    # allow user to turn off calculator
    if cal_action.lower() == 'quit':
        On = False
        break

    # perform calculator operations - logic

    # division
    if cal_action.lower() == 'divide':
        # convert to whole number
        if num_1 >= num_2:
            cal_sum = division(num_1, num_2)
            print(int(cal_sum))
        # decimals total
        else:
            print(cal_sum)
    # addition
    elif cal_action.lower() == 'add':
        cal_sum = addition(num_1, num_2)
        print(cal_sum)
    # subtraction
    elif cal_action.lower() == 'subtract':
        cal_sum = subtraction(num_1, num_2)
        print(cal_sum)
    # multiplication
    elif cal_action.lower() == 'multiply':
        cal_sum = multiplication(num_1, num_2)
        print(cal_sum)
    # pie
    elif cal_action.lower() == 'pi':
        cal_sum = pi(num_1)
        print(cal_sum)
    # expoenet ^ 2
    elif cal_action.lower() == 'exponent':
        cal_sum = expo(num_1, exponent=2)
        print(cal_sum)
    # cube ^ 3
    elif cal_action.lower() == 'cube':
        cal_sum = cube(num_1)
        print(cal_sum)
        # decimal
    elif cal_action.lower() == 'decimal':
        cal_sum = decimal(num_1)
        print(cal_sum)
    

    # give user the option to clear the total results
    if cal_action.lower() == 'clear':
        clear(cal_sum)
