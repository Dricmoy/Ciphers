#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2025 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 1 Student Solution
January 2025
Author: Dricmoy Bhattacharjee
"""


import string
from sys import flags


LETTERS = ''.join([u+l for u, l in  
    zip(string.ascii_uppercase, string.ascii_lowercase)]) # a string of Capital-Lower case alternating letters from a-z


def get_map(letters=LETTERS):
    char_to_index, shift_to_char = {}, {} #Defining the dictionaries that will store the mappings
    
    # mapping a pair of characters and their shifts
    for index, chars in enumerate(letters): #enumerate is a function provided by python that returns [index, value] of a list each iteration
        char_to_index[chars] = index #each character is mapped based on their indexes
        shift_to_char[index] = chars
    
    return char_to_index, shift_to_char

def encrypt(message: str, key: str):
    encrypted_message = list(message) #convert from string to list for mutability
    shiftdict, letterdict= get_map() 

    for index, char in enumerate(encrypted_message):
        if (index != 0):
            key = message[index-1] #so the previous letter
            while (not key.isalpha()): #so while we hit punctuations
                index -= 1
                key = message[index-1] #try the letter before it
            
        if (char.isalpha()): #check if its not special letters
            encrypted_message[index] = letterdict[(shiftdict[char] + shiftdict[key]) % 52]
            #I need to %52 so it doesn't go out of bounds and wraps around letterdict, for ex:- 'c' + 'x' = 5 + 47 = 52 (wraps to 0) 
            
    return ''.join(encrypted_message) #make it into a string again


def decrypt(message: str, key: str):
    decrypted_message = list(message) #convert from string to list for mutability
    shiftdict, letterdict = get_map() 
    
    for index, char in enumerate(decrypted_message): 
        if (char.isalpha()): #check if its not special letters
            decrypted_message[index] = letterdict[(shiftdict[char] - shiftdict[key]) % 52]
            #I need to %52 so it doesn't go out of bounds and wraps around letterdict, for ex:- 'c' + 'x' = 5 + 47 = 52 (wraps to 0) 
          
    return ''.join(decrypted_message) #make it into a string again

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert decrypt(encrypt("AaBbCcDd...", "y"), "y") == "AaBbCcDd..."

if __name__ == "__main__" and not flags.interactive:
    test()