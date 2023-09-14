import string

'''
def minion_game(string):
    kevin_points = 0
    stuart_points = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = 'aeiou'
    consonants_substrings = []
    vowels_substrings = []

    for i, c in enumerate(string):
        if c.upper() in vowels:
            substring = string[:i]
            vowels_substrings.append(substring)
            kevin_points +=1
            i +=1

        else:
            substring = string[:i]
            consonants_substrings.append(substring)
            stuart_points +=1
            i +=1
    
    if kevin_points > stuart_points:
        print(f"Kevin {kevin_points}")
    elif kevin_points < stuart_points:
        print(f"Stuat {stuart_points}")
    else:
        print("Draw")
    '''

def minion_game(string):
    kevin_points = 0
    stuart_points = 0
    vowels = 'AEIOU'

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_points += len(string) - i
        else:
            stuart_points += len(string) - i

    if kevin_points > stuart_points:
        print(f"Kevin {kevin_points}")
    elif kevin_points < stuart_points:
        print(f"Stuart {stuart_points}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input('enter a word: ')
    minion_game(s)
