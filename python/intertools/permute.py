#Print the permutations of the string  on separate lines.

from itertools import permutations

str_line = input().split()

answr = list(permutations(sorted(str_line[0]), int(str_line[1]))) 

for ch in answr:
    print(''.join(ch))