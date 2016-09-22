"""
*****************************************************
Kata challenge 9-2-16

ToLeetSpeak

Leet = 1337
Given alphabet, write dictionary to translate English

*****************************************************
"""

def Leetspeak(StrInput):
    newstring = ""
    mydict = {'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3', 'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!',
              'J' : 'J', 'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0', 'P' : 'P', 'Q' : 'Q', 'R' : 'R',
              'S' : '$', 'T' : '7', 'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y', 'Z' : '2'}

    for i in range(len(StrInput)):
        if mydict.get(StrInput[i]) == None:
            newstring += StrInput[i]
        else:
            newstring += mydict[StrInput[i]]
    print newstring
    return

Leetspeak("HELLO, MY NAME IS JUSTIN ZHOU.")