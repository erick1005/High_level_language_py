from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    # Write your code here
    words = str.split(' ')
    result = [word[0].upper() + word[1:]if word else '' for word in words]
    return ' '.join(result)
    