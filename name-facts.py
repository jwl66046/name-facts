#!/usr/bin/env python3

'''
Name facts program.

A simple app that I am developing to work on Python skills.

~JwL 2017
'''

## Declare variables
first_name = ""
last_name = ""
total_letters = None
alphabet = "abcdefghijklmnopqrstuvwxyz"


## create functions

def next_section():
    input("\n\tPress the enter key to continue\n")

def parse_letters():
    d = {}
    x = str(total_letters)


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
print("\nYour name is: {} {}".format(first_name, last_name))
next_section()


## Total number of letters in their name
total_letters = len(first_name) + len(last_name)
print("{}, your name has {} letters in it!".format(first_name, total_letters))
next_section()


## Occurences of each letter in name

letter_count = first_name.lower() + last_name.lower()

print("{}, here is the number of times each letter is used in your name:\n\n".format(first_name))

for key in alphabet:
	if letter_count.count(key) != 0:
		print(key, letter_count.count(key))
next_section()
