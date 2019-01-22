'''
Task
You are given a string s. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of that contains 2 or more vowels.
Also, these substrings must lie in between consonants and should contain vowels only.

Note:
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format
A single line of input containing string s.

Output Format
Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.
'''
import re

VOWELS = r'AEIOUaeiou'
CONSONANTS = r'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

r = r'[%s]([%s]{2,})(?=[%s])' % (CONSONANTS, VOWELS, CONSONANTS)

group = re.findall(r, input())
print(group if group else "-1")

'''
Sample Input
rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output
ee
Ioo
Oeo
eeeee
'''
