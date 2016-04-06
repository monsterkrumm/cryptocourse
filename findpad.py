# python script for finding the first padding byte in the ciphertext
# Coursera crypto course, programming assignment week 3
# Marc Watkins
# 2015-04-13

from oracle import *
from values import orig, origlist, defbl
import sys

data = ""

if len(sys.argv) >= 2:
    try:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
        print "Loaded data from file %s successfully." % sys.argv[1]

    except IOError:
        print "Error opening specified file: " + sys.argv[1]

iv = origlist[:defbl]
qbytes = origlist [defbl:]

Oracle_Connect()

print "Testing with original data given by course."
test = Oracle_Send(origlist,3)
print "Server responded: %d" % test
if test == 1:
    print "Success!"
else:
    print "Hm, this didn't work, but continuing regardless..."

for i in range(defbl):
    if qbytes[i] == 0:
        qbytes[i] = 1
    else:
        qbytes[i] = 0
    response = Oracle_Send(iv+qbytes,3)
    if response == 1:
        print "Server checked byte " + str(i) + " and responded " + str(response)
    else:
        print "Server checked byte " + str(i) + " and responded " + str(response)
        print "Thus we have found the padding length: " + str(defbl - i)
        break

Oracle_Disconnect()
