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

from typing import List
from a2p3 import decryptMessage

def decryptMystery() -> str:
    with open('mystery.txt', 'r', encoding='utf-8') as file:
        to_decipher = file.read()
    
    key = [8,1,6,2,10,4,5,3,7,9] #hardcoding from p4 description
    decrypted_message = decryptMessage(key, to_decipher)
    
    with open('mystery.dec.txt', 'w', encoding='utf-8') as file:
        file.write(decrypted_message)
    
    return decrypted_message
    
def test():
    assert decryptMessage([2, 4, 1, 5, 3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
