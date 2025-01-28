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
CMPUT 331 Assignment 2 Student Solution
January 2025
Author: Dricmoy Bhattacharjee
"""

def encryptMessage(key: int, message: str) -> str:
    res = ['' for _ in range(key)] #empty strings
    
    count = 0 #new rails
    rail_direction = 1 #dir of movement
    
    for chars in message:
        res[count] += chars
        
        if count == 0: #at the top rail, change direction
            rail_direction = 1
        elif count == key - 1: #bottom rail
            rail_direction = -1
        count += rail_direction #the direction we moved towards
        
    return ''.join(res)

def decryptMessage(key: int, message: str) -> str:
    rail_lengths = [0] * key
    rail = 0
    direction = 1 
    for char in message:
        rail_lengths[rail] += 1
        if rail == 0:
            direction = 1
        elif rail == key - 1:
            direction = -1
        rail += direction

    rails = ['' for _ in range(key)]
    index = 0
    for i in range(key):
        rails[i] = message[index:index + rail_lengths[i]]
        index += rail_lengths[i]

    decrypted_message = []
    rail = 0
    direction = 1 
    for _ in range(len(message)):
        decrypted_message.append(rails[rail][0])
        rails[rail] = rails[rail][1:]  
        if rail == 0:
            direction = 1
        elif rail == key - 1:
            direction = -1
        rail += direction

    return ''.join(decrypted_message)

def test():
    assert decryptMessage(2, encryptMessage(2, "SECRET")) == "SECRET"
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"
    assert decryptMessage(4, encryptMessage(4, "HELLO WORLD")) == "HELLO WORLD"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
