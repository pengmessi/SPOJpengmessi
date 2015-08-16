__author__ = 'pengmessi'
"""
ID: 4
URL: http://www.spoj.com/problems/ONP/

ONP - Transform the Expression
no tags
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

Input

t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output

The expressions in RPN form, one per line.
Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
"""

def transformed(s):
    if s[0] == '(' and s[-1] == ')':
        s = s[1:-1]
    else:
        return s

    level = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1
        if ch in ['+','-','*','/','^'] and level == 0:
            return transformed(s[:i]) + transformed(s[i+1:]) + ch



if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        print(transformed(s))
