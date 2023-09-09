# Nathan Reid
# Oct. 13th, 2022
# Create a login


import getpass

# while True:

# prompt the user for their choice from the options
selection = input("\nThis is a login page. \n\nWhat option do you choose? \nCreate account \nForgot password \nForgot username \nLogin\n\n")
    
if selection.lower() == 'create account':
    print("Please, enter the following information. ")

    # insert the user information in the text file
    with open('user-info.txt', 'a') as f:
        user_n = input("Username: ")
        f.write("Username: " + user_n + "\n")
        # make sure the password does not echo for user protection
        pass_w = getpass.getpass(prompt = "Password: ")
        f.write("Password: " + pass_w + "\n")
        f_name = input("First Name: ")
        f.write("First Name: " + f_name + "\n")
        l_name = input("Last Name: ")
        f.write("Last Name: " + l_name + "\n")
        email = input("Email: ")
        f.write("Email: " + email + "\n")
        state = input("State: ")
        f.write("State: " + state + "\n")
        security_q = input("Create security question: ")
        f.write("Security Question: " + security_q + "\n")
        security_a = input("Security Question Answer: ")
        f.write("Security Answer: " + security_a + "\n" )
        # make sure the confirm password does not echo for user protection
        confirm_p = getpass.getpass(prompt = "Confirm Password: ")
        f.write("\n")


    # if the confirm password and password don't match prompt user to re-enter
    while confirm_p.lower() != pass_w.lower():
        print("Your confirm password does not match your password. Re-enter. ")
        confirm_p = input("Confirm Password: ")


    # check to make sure the confirm password and password match
    if confirm_p.lower() == pass_w.lower():
        pass


if selection.lower() == 'forgot password':
    # ask user for username to use to locate user information in the text file
    username_answer = input("What is your username? ")
    with open('user-info.txt', 'r') as f:
        lines = f.read()
        # check to see if user answer(username) in text file
        if username_answer in lines:
            # change the data type from string to list
            new = lines.splitlines()
            # 'Username' is constant for all users. Add 'Username' to user input for the answer to be identical to element in list
            check_username = "Username: " + username_answer
            # find the index of the username
            index = new.index(check_username)
            # find the index of the security question
            question_index = index + 6
            # find the index of the security answer
            answer_index = question_index + 1
            # change the security question into an input to get user response
            SQ = new[question_index]
            # ask the user the security question
            ask = input(SQ)
            # use this variable to add string to compare the user input plus 'Security Answer' to elements in list
            add = 'Security Answer: ' + ask
            # check to see if answer is in the text file list
            if add in new:
                # find the index of the START point of the information you want to retrive
                i = index + 1
                # find the index of the END point of the information you want to retrive
                # inform the program how many times to iterate while collection information to print
                l = i + 1
                for i in range(i,l):
                    print("Your password is " + (new[i][10:]) + ".")        
            else:
                # if securty answer is wrong print this. 
                print("Wrong security answer. Re-enter.")
        else:
            # if the username is wrong and not in the text file at all
            print("Failed. Try again.")


while selection.lower() == 'forgot username':
    password_answer = input("What is your password? ")
    with open('user-info.txt', 'r') as f:
        # read the text file information as a string
        lines = f.read()
        # check to see if the password is in the file
        if password_answer in lines:
            # change the data type from string to list
            new = lines.splitlines()
            # add 'password' to the user input to comapre to the exact list element
            check_pass_pwd = 'Password: ' + password_answer
            # find the index in the text file of the password
            index = new.index(check_pass_pwd)
            # start point for the information to print
            i = index - 1
            # END point of the information to print and how many iterations to do
            k = i + 1
            # loop through file to print the information
            for i in range(i,k):
                print("Your username is " + (new[i][10:]) + ".")
        else:
            print("Fail. Re-enter.")


# NOTE - DELETE the first two empty lines in the text file to work


while selection.lower() == 'login':
    # prompt user to put in account credentials
    login_name = input("Username: ")
    login_pwd = input("Password: ")
    # open the text file and read each line
    with open('user-info.txt', 'r') as f:
        # information in text file is a string
        lines = f.read()
        # check to see if the username and password is in the text file
        if login_name in lines and login_pwd in lines:
            # change text file information to a list and get rid of '\n'
            new = lines.splitlines()
            # The login_name by itself will not seen in new(list)
            # added the string 'Username' + login_name for the list to see it
            check_name = 'Username: ' + login_name
            # use index() to find the index of the login_name in the list
            index = new.index(check_name)
            # The profile information STARTS 2 indexes from the username
            # i = ('Username: ' + login_name) + 2
            i = index + 2
            # The profile information ENDS 4 indexes from the username
            j = i + 4
            # Use user profile start and end point in for loop
            # tell the program where to start and finish in the text file
            for i in range(i,j):
                # print user information line
                print('\t' + new[i])
            break
        else:
            print("Login failed. Please, re-enter. ")


     




