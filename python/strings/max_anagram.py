from collections import Counter

def getMinimumAnagramDifference(str1, str2):
    # Write your code here.
    if sorted(str1) == sorted(str2) and len(str1) == 1:
        return 0
    elif len(str1) == 1 and len(str2) == 1:
        return 1
    else:
        Counter1 = Counter(str1)
        Counter2 = Counter(str2)

        diff = Counter1 - Counter2 + Counter2 - Counter1
        mindiff = sum(diff.values())
        
        return mindiff