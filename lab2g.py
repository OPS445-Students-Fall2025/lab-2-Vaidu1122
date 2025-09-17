#!/usr/bin/env python3

# Author: Vaidehi Patel
# Author ID: 166249219
# Date Created: 2025/09/17
# Course: OPS 445 NDD

import sys

if len(sys.argv) == 1:
#    print("No arguments!")
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1
    print("blast off!")
    sys.exit()

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
    print("blast off!")
    sys.exit()

if len(sys.argv) > 2:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
    print("blast off!")
    sys.exit()


