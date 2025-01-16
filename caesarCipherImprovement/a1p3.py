#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2025 Dricmoy Bhattacharjee
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
    shiftdict, letterdict= SHIFTDICT, LETTERDICT
    
    key_index = 0
    len_key = len(key) #so don't have to repeat this many times, saves computation
    
    #must ignore all punctuations
    for index, char in enumerate(encrypted_message):
        if (char.isalpha()): #check if its not special letters
            encrypted_message[index] = letterdict[(shiftdict[char] + shiftdict[key[key_index % len_key]]) % 52]
            #doing modulo by length of the key string to wrap around from, 0 to length of key to not go out of bounds
            key_index += 1
            
    return ''.join(encrypted_message) #make it into a string again

def decrypt(message: str, key: str):
    decrypted_message = list(message) #convert from string to list for mutability
    shiftdict, letterdict= SHIFTDICT, LETTERDICT
    
    key_index = 0
    len_key = len(key) #so don't have to repeat this many times, saves computation
    
    for index, char in enumerate(decrypted_message): 
        if (char.isalpha()): #check if its not special letters
            decrypted_message[index] = letterdict[(shiftdict[char] - shiftdict[key[key_index % len_key]]) % 52]
            #doing modulo by length of the key string to wrap around from, 0 to length of key to not go out of bounds 
            key_index += 1
            
    return ''.join(decrypted_message) #make it into a string again

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

if __name__ == "__main__" and not flags.interactive:
    test()