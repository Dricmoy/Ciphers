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

def encryptMessage(key: List[int], message: str) -> str:
    num_columns = len(key)
    num_rows = (len(message) + num_columns - 1) // num_columns
    grid = ['' for _ in range(num_rows)]
    
    for i, char in enumerate(message):
        grid[i // num_columns] += char
    
    encrypted_message = ''
    grid_transpose = [[''] * len(grid) for _ in range(len(grid[0]))]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid_transpose[j][i] = grid[i][j]
    
    for i in key:
        encrypted_message += ''.join(grid_transpose[i-1])
    return encrypted_message

def test():
    assert encryptMessage([2, 4, 1, 5, 3], "CIPHERS ARE FUN") == "IS HAUCREERNP F"
    assert encryptMessage([1, 3, 2], "ABCDEFG") == "ADGCFBE"
    assert encryptMessage([2, 1], "HELLO WORLD") == "EL OLHLOWRD"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
