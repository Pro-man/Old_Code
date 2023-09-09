# Nathan Reid
# 12/15/22
# Creating a digital clock while using functions


import time 
from datetime import datetime, date


# Date
def today():
    '''Display the current date.'''
    now = date.today()
    td = now.strftime("%B %d, %Y")
    print("Today is " + td + ".")


# Time
def display():
    '''Display the time for the digital clock.'''
    while True:
        watch = time.strftime("%I:%M:%S %p")
        print("The current time is >", watch, end='\r')
        time.sleep(1) 
        

today()
display()