'''
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z,A-Z,0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''
import re


def validate_UID(UID: str) -> str:
    pattern1 = r'(?=(.*[A-Z]){2})(?=(.*[0-9]){3})(?=^[A-Za-z0-9]{10}$)'
    pattern2 = r'^.*(.).*\1.*$'
    return "Valid" if re.search(pattern1, UID) and not re.search(pattern2, UID) else "Invalid"


for _ in range(int(input())):
    print(validate_UID(input()))

# print(validate_UID("AV12345678"))
# print(validate_UID("V12345678V"))
# print(validate_UID("A324"))

'''
Input Format
The first line contains an integer , the number of test cases.
The next lines contains an employee's UID.

Output Format
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid

'''
