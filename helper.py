# helper functions
# coursera crypto course week 3 programming assignment
# Marc Watkins
# 2015-04-13

def makeDeltaBlock(b, bl, k=0):
    assert bl - (b+k) >= 0
    starter = [0]*(bl-(b+k)) + [b+k]*(b+k)
    next = [0]*(bl-(b+k)) + [b+k+1]*(b+k)
    delta = [x^y for x,y in zip(starter,next)]
    return delta


def xorLists(l1, l2):
    assert len(l1) == len(l2)
    return [a^b for a,b in zip(l1,l2)]


def checker(d):
    print "calling checker"
    assert d[0] == 0

    for i in range(16):
        if d[i] != 0:
            i = i - 1
            break

    print "Position is " + str(i)

    from values import origlist, defbl as bl
    import oracle
    iv = origlist[:bl]
    c1 = origlist[bl:bl*2]
    c2 = origlist[bl*2:]

    oracle.Oracle_Connect()
    for value in range(256):
        d[i] = value
        newc1 = [x^y for x,y in zip(d,c1)]
        submission = iv+newc1+c2
        response = oracle.Oracle_Send(submission,3)
        if response == 1:
            oracle.Oracle_Disconnect()
            return value
    oracle.Oracle_Disconnect()
    return -1

def ivch(d):
    print "Calling ivch"
    for i in range(16):
        if d[i] != 0:
            i = i - 1
            break

    print "position  is " + str(i)

    from values import origlist, defbl as bl
    import oracle
    iv = origlist[:bl]
    c1 = origlist[bl:bl*2]

    oracle.Oracle_Connect()
    for value in range(256):
        d[i] = value
        ivnew = [x^y for x,y in zip(d,iv)]
        response = oracle.Oracle_Send(ivnew+c1,2)
        if response == 1:
            oracle.Oracle_Disconnect()
            return value
    print "No value found, something went wrong"
    oracle.Oracle_Disconnect()
