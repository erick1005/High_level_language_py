import textwrap
import string 

#the function takes a string wraps it into k (or we can say splits) characters and prints without duplicates
# string AABCAAADA k = 3

def merge_tool(string, k):
    string_split = textwrap.wrap(string, k)
    answer = []
    for word in string_split:
        results = ""
        for c in word:
            if c not in results:
                results+= c
        answer.append(results)
        print(results)
    #print(answer)

    #word1 = string_split[0]
    #word2 = string_split[1]
    #word3 = string_split[2]

if __name__ == '__main__':
    s = input('input string: ')
    k = int(input('input divisor: '))

    merge_tool(s, k)
