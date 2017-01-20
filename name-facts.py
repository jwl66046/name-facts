#!/usr/bin/env python3

'''
Name facts program.

A simple app that I am developing to work on Python skills.

~JwL 2017
'''

## Define variables

first_name = ""
last_name = ""


## create functions

def next_section():
    input("\n\tPress the enter key to continue\n")


###########################
##### Begin Program  ######
###########################

## Get user name
print("\n\nWelcome to John's Name Facts Program!")
next_section()

while not first_name:
    first_name = input("Please enter your first name: ")
while not last_name:
    last_name =  input("Please enter your last name: ")


## Return name
print("Your name is: " + first_name + " "+ last_name)
# input("\n\tPress the enter key for more facts!")
next_section()


## Total number of letters in their name
total_letters = len(first_name) + len(last_name)
print(first_name + ", your name has " + str(total_letters) + " letters in it!")
next_section()


