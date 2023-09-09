# Nathan Reid
# Oct. 5th, 2022
# Create a random password genrator

from string import ascii_letters, digits, punctuation
from random import choice

# create empty list
pass_w = []

print("Enter 0 to end.")

# while loop
while 8 or 16 or 32 != length:

    # Ask user how long they want their password
    length = int(input("Would you like for your password to be 8, 16, or 32 characters: "))
    
    # password length logic
    if length == 8:
        # iterate the number of times the length of the password
        for num in range(0,8):
            # use and join letters and numbers in the password and put in a variable
            e = ''.join([choice(ascii_letters + digits + punctuation)])
            # append each password character into the empty list
            pass_w.append(e)
        print("\nYour new random password is below: ")
        # print the elements in the list
        print(*pass_w)
        # Delete old password to allow on new password to display
        pass_w.clear()
    # NOTE - (*) symbol is used to print the list elements in a single line with space. 
    elif length == 16:
        for num in range(0,16):
            e = ''.join([choice(ascii_letters + digits + punctuation)])
            pass_w.append(e)
        print("\nYour new random password is: ")
        print(*pass_w)
        pass_w.clear()
    elif length == 32:
        for num in range(0,32):
            e = ''.join([choice(ascii_letters + digits + punctuation)])
            pass_w.append(e)
        print("\nYour new random password is below: ")
        print(*pass_w)
        pass_w.clear()
    elif length == 0:
        break
print(pass_w)
        



