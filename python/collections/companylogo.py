from collections import Counter

if __name__ == '__main__':
    s = input().lower()
    data = Counter(s)

    '''the ord() function, which returns the ASCII code of a character, and negate that instead of the character itself'''

    counts = sorted(data.most_common(3), key=lambda pair: (pair[1], -ord(pair[0])), reverse=True)
    #print(dict(counts))
    
    for Key, Value in counts:
        print(Key, Value)

# solution 2
# easier way to solve it.....

S = input()
S = sorted(S)

data = Counter(list(S))
for k, v in data.most_common(3):
    print(k, v)