# checking for the longest palindrome in a string function

def longest_palindrome(self, s: str) -> str:
    result = ''
    result_len = 0

    for i in range(len(s)):
        l, r = i, i
        #odd number palindrome
        while l >= 0 and r < len(s) and s[l] == s[r]: #checks palindrome
            #checks len of palindrome substr
            if (r - l + 1)> result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            l -= 1
            r += 1

        #even number palindrome
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]: #checks palindrome
            #checks len of palindrome substr
            if (r - l + 1)> result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            l -= 1
            r += 1
    return result
        