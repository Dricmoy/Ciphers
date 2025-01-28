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

import math
from typing import List

def decryptMessage(key: List[int], message: str) -> str:
    numOfRows = math.ceil(len(message) / len(key)) # I don't know if I'm allowed to import math.ceil but saw it in the course material
    numOfColumns = len(key)

    grid = [[''] * numOfColumns for _ in range(numOfRows)]
    
    index = 0
    for row in range(numOfRows):
        for col in range(numOfColumns):
            if not index < len(message):
                grid[row][col] = 'S#HADED'
            index += 1
        
    ordered_columns = [0] * numOfColumns
    for i, k in enumerate(key):
        ordered_columns[k - 1] = i 
    
    shifted_grid = [[''] * numOfColumns for _ in range(numOfRows)]
    for col in range(numOfColumns):
        new_col = ordered_columns[col]
        for row in range(numOfRows):
            shifted_grid[row][new_col] = grid[row][col]
    
    index = 0
    for col in range(numOfColumns):
        for row in range(numOfRows):
            if index < len(message) and shifted_grid[row][col] != 'S#HADED':
                shifted_grid[row][col] = message[index]
                index += 1
    
    grid_transpose = [[''] * len(shifted_grid) for _ in range(len(shifted_grid[0]))]

    for i in range(len(shifted_grid)):
        for j in range(len(shifted_grid[i])):
            grid_transpose[j][i] = shifted_grid[i][j]
    
    #just gonna order the columns properly and read into string (now as rows in the matrix)
    unshifted = [[''] * len(shifted_grid) for _ in range(len(shifted_grid[0]))]
    for index, row in enumerate(grid_transpose):
        unshifted[key[index]-1] = row
    
    unshifted_transpose = [[''] * len(unshifted) for _ in range(len(unshifted[0]))]
    for i in range(len(unshifted)):
        for j in range(len(unshifted[i])):
            unshifted_transpose[j][i] = unshifted[i][j]
            
    plaintext = ''
    for row in range(len(unshifted_transpose)):
        for col in range(len(unshifted_transpose[row])):
            if unshifted_transpose[row][col] != 'S#HADED':
                plaintext += unshifted_transpose[row][col]
                
    return plaintext

def test():
    assert decryptMessage([2, 4, 1, 5, 3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"
    assert decryptMessage([1, 3, 2], "ADGCFBE") == "ABCDEFG"
    assert decryptMessage([2, 1], "EL OLHLOWRD") == "HELLO WORLD"
    
from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
