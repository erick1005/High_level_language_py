from itertools import groupby

def count_charmessage(message):
    res= ''
    i = 0
    while i < len(message):
        count = 1
        while i + 1 < len(message) and message[i] == message[i+1]:
            i += 1
            count += 1
        res += message[i] + str(count)
        i += 1
    return res

message = 'abbdcaamessage'
print(count_charmessage(message))

"""
def count_chars(s):
    return ''.join(f'{char}{len(list(group))}' for char, group in groupby(s))

str = 'abbdcaas'
print(count_chars(str))
"""