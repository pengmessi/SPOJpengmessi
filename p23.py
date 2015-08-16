__author__ = 'pengmessi'
"""
URL: http://www.spoj.com/problems/PIR/

PIR - Pyramids
no tags
Recently in Farland, a country in Asia, the famous scientist Mr. Log Archeo discovered ancient pyramids. But unlike those in Egypt and Central America, they have a triangular (not rectangular) foundation. That is, they are tetrahedrons in the mathematical sense. In order to find out some important facts about the early society of the country (it is widely believed that the pyramid sizes are closely connected with Farland's ancient calendar), Mr. Archeo needs to know the volume of the pyramids. Unluckily, he has reliable data about their edge lengths only. Please, help him!

Input

t [number of tests to follow] In each of the next t lines six positive integer numbers not exceeding 1000 separated by spaces (each number is one of the edge lengths of the pyramid ABCD). The order of the edges is the following: AB, AC, AD, BC, BD, CD.

Output

For each test output a real number - the volume, printed accurate to four digits after decimal point.

Example

Input:


2
1 1 1 1 1 1
1000 1000 1000 3 4 5

Output:


0.1179
1999.9937
"""
import math

if __name__ == '__main__':
    n = int(input())
    while n:
        n -= 1
        a, c, e, b, f, d = map(int, input().split())
        y = (a*a + c*c - b*b) / (2*c)
        x = math.sqrt(a*a - y*y)
        q = (c*c + e*e - d*d) / (2*c)
        p = (a*a + e*e - f*f - 2*q*y) / (2*x)
        r = math.sqrt(e*e - q*q - p*p)
        V = c * x * r / 6
        print(round(V,4))