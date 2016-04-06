# Python script to find the next byte, given a padder value
# Coursera crypto course week 3 programming assignment
# Marc Watkins
# 2015-04-13

import sys
from oracle import *
from values import orig, origlist, defbl, defpadder
from helper import makeDeltaBlock, xorLists

bl = defbl # here could be code to take bl from sys.argv
iv = origlist[:bl]
c1 = origlist[bl:bl*2]
c2 = origlist[bl*2:]
# print iv, c1, c2

if len(sys.argv) < 2:
    b = defpadder 
else:
    b = int(sys.argv[1])
    if b < 0 or b > 16:
        print "Invalid padder value, using default."
        b = defpadder


p2sofar = [-1,-1,-1,-1,-1,11,11,11,11,11,11,11,11,11,11,11]


for i in range(bl-b):

    deltaBlock = makeDeltaBlock(b,bl,i)
    print deltaBlock

    r = checker(deltaBlock)
    
    for value in range(256):
        deltaBlock[-b-i-1] = value
        newc1 = xorLists(deltaBlock,c1)
        submission = iv + newc1 + c2  
        response = Oracle_Send(submission,3)
        print "For " + str(value) + " we get server response " + str(response)
        if response == 1:
            print "Found match for value  = " + str(value)
            break

    found = (b+i+1)^value
    print "So we found plaintext byte value " + str(found) \
            + " which is the character '" + chr(found) + "'"
    p2sofar[-(b+i)] = found
    print p2sofar


