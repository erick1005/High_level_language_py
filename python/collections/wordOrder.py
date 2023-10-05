#a programe that counts distinct words and print the number of occurence of each word

from collections import Counter

n = int(input())
no_0f_distinct_word = 0
words = []
for _ in range(n):
    word = input()
    words.append(word)

no_of_occr = dict(Counter(words))

no_0f_distinct_word = len((set(words)))
print(no_0f_distinct_word)
#print(no_of_occr)
for value in no_of_occr.values():
    print(value, end=' ')
