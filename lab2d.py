#!/usr/bin/env python3

# Name: Vaidehi Patel
# OPS 445 NDD
# Std ID: 166249219

# Lab 2 Script 4 - Lab 2 d

import sys

#name = input('Name: ')
#name = sys.argv[1]

#age = int(input('Age: '))
#age = int(sys.argv[2])

#name = sys.argv[1]
#age = int(sys.argv[2])

#if len(sys.argv) == 0:
#    print('Zero command-line arguments are present.')
''' for self learning:
The above is wrong because, sys.argv always has atleast 1 element, which is script name, hence the minimum length of sys.argv would always be 1. Hence, the condition, sys.argv == 0 would never be true.
'''

# Expecting 0 arguments.
if len(sys.argv) == 1:
    #print("Usage: Zero command line arguments provided while running the script ", sys.argv[0])
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

# Expecting 1 argument.
if len(sys.argv) == 2:
    #print("Usage: " + sys.argv[0] + " " + sys.argv[1] + " age")
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

# Expecting 2 arguments.
if len(sys.argv) == 3:
    #print('Usage: Two arguments are provided when running the script ', sys.argv[0])
    #print("Usage: " + sys.argv[0] + " " + sys.argv[1] + " " + sys.argv[2])
    #sys.exit()

    name = sys.argv[1]
    age = int(sys.argv[2])

    print("Hi " + name + ", you are " + str(age) + " years old.")

    sys.exit()

# More than 2 arguments.
if len(sys.argv) > 3:
    #print('Usage: More than two command-line arguments are provided while running the script ', sys.argv[0])
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()