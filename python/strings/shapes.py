#printing letters can be used to print (caps) lowr upper and digits
'''n = 1
for letters in string.ascii_lowercase:
  if n < 5:
    print(letters)
  n = n + 1'''

#right justify or allign
'''n = 1
for c in string.ascii_lowercase:
    if n < 6:
        print(c.rjust(4,'-'))
    n += 1'''

#creating simple rectangle
'''len = 8
width = 4

for i in range(1, width + 1):
  for j in range(1, len + 1):
    print('*',end='')
  print()'''

#creating a triangle.
'''tall = 8

for i in range(1, tall + 1):
  print(('*' * i).rjust(8))
'''
#isosceles triangle  
'''tall = 8

for i in range(1, tall + 1):
  print(' ' * (tall - i) + '*' * (2 * i - 1))'''

#star shaped
tall = 8

for i in range(tall):
  print(' ' * (tall - i -1) + '*' * (2 * i + 1))
for j in range(tall - 2, -1, -1):
  print(' ' * (tall - j -1) + '*' * (2 * j + 1))