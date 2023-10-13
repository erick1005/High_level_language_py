 #importing the groupby function from itertools
from itertools import groupby

# taking the input from the user
s = input()

# looping over the tuples returned by groupby
for k, g in groupby(s):
    # printing the output in the desired format
    print(f"({len(list(g))}, {int(k)})", end=" ")

"""this input 1222311 will produce
(1, 1) (3, 2) (1, 3) (2, 1) """