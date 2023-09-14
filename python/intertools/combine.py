#Print the different combinations of string  on separate lines.

from itertools import combinations

str_s = input().split()

iterable = sorted(str_s[0])
length = int(str_s[1])

results = []
for r in range(1, length + 1):
    results.extend(combinations(iterable, r))

for ch in results:
    print(''.join(ch))
