'''
Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5

Number must contain at least decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . symbol.
'''
import re

for _ in range(int(input().strip())):
    print(bool(re.search(r'^[+\-]?[0-9]*\.[0-9]+$', input().strip())))
    # print(bool(re.match(r'[+\-]?[0-9]*\.[0-9]+$', input().strip())))

'''
Sample Input 0
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0
False
True
True
False
'''
