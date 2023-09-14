#we can use .format() to format a string, :o-octal, :d-decimal, :x-hexadecimal, :b-binary
#decimal_number = []
def print_fmt(number):
   width = len('{:b}'.format(n)) #space-padded to match the width of the binary value
   for number in range(1,n+1):
        print('{:>{width}d} {:>{width}o} {:>{width}X} {:>{width}b}'.format(number, number, number, number, width=width))
    
#This function uses the format() method to specify the alignment and width of each column. The > character is used to right justify the text within a field of width 10 characters.
#^ centers the txt
#< left justify the text

if __name__ == '__main__':
  n = int(input())
  print_fmt(n)

'''number = 30
print('Binary: {:b}'.format(number))
print('octal: {:o}'.format(number))
print('hexadec: {:x}'.format(number))
print('decimal: {:d}'.format(number))'''