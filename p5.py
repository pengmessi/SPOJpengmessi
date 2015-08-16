__author__ = 'pengmessi'
"""
PALIN - The Next Palindrome
no tags

A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to
right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the
smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.

Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

Output

For each K, output the smallest palindrome larger than K.

Example

Input:
2
808
2133

Output:
818
2222

Warning: large Input/Output data, be careful with certain languages

98999
"""
import sys

def greater(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    else:
        for i in range(len(a)):
            if not a[i] == b[i]:
                return int(a[i]) > int(b[i])
        return False


def all9(s):
    for ch in s:
        if not ch == '9':
            return False
    return True


def nextone(s):
    i = len(s) - 1
    while i >= 0 and s[i] == '9':
        i -= 1
    ch = chr(ord(s[i]) + 1)
    return s[:i] + ch + "0" * (len(s) - i - 1)


def theNextPalindrome(s):
    left = s[:len(s)//2]
    if len(s) % 2 == 0:
        k = left + left[::-1]
        if greater(k, s):
            return k
        elif not all9(left):
            l = nextone(left)
            return l + l[::-1]
        else:
            return "1"+"0"*(len(s)-1)+"1"
    else:
        k = left + s[len(s)//2] + left[::-1]
        if greater(k, s):
            return k
        elif not all9(left + s[len(s)//2]):
            l = nextone(left + s[len(s)//2])
            #print(left + s[len(s)//2])
            #print("l = ", l)
            return l + l[-2::-1]
        else:
            return "1"+"0"*(len(s)-1)+"1"

if __name__ == '__main__':
    n = int(input())
    while n:
        n -= 1
        snum = input()
        print(theNextPalindrome(snum))