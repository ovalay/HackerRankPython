#!/bin/python3

import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":            
            print ("12"+s[2:-2])
        else:
            prefix=int(s[:2])+12
            print("%s%s" % (str(prefix), s[2:-2]))
    else:
        if s[:2] == "12":            
            print("00"+s[2:-2])
        else:
            print(s[:-2])

s = input()

result = timeConversion(s)


