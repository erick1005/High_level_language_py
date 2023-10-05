import re
T = int(input())
for _ in range(T):  
    try:
        if True:
          s = input()
          result = (re.compile(s))
          print(bool(result))
        else:
            print('False')
    except re.error:
        print('')