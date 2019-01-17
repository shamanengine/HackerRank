# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

'''
Sample Input
..12345678910111213141516171820212223

Sample Output
1
'''
