import string
# Rangoli is a form of Indian folk art based on creation of patterns

def print_rangoli(size):
  alphabet_char = string.ascii_lowercase
  for i in range(size-1, -size, -1):
      row = ['-'] * (4 * size - 3)
      for j in range(0, size - abs(i)):
            row[2*(size-1) + 2*j] = alphabet_char[abs(i) + j]
            row[2*(size-1) - 2*j] = alphabet_char[abs(i) + j]
      print(''.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

