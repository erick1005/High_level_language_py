from itertools import combinations_with_replacement

data = input().split()

combine = list(combinations_with_replacement(sorted(data[0]), int(data[1])))

for data in combine:
    print(''.join(data))
