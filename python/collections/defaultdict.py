# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

#reads a series of keys from STDIN, keeps track of what line each key was on, and then for a second series of keys, it prints out what lines those keys were seen on in the first part.

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(d[input()]) or -1)