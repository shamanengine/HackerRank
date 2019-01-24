'''
Sample Input
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output
DEXTER <dexter@hotmail.com>

Input
4
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>

Expected Output
this <is@valid.com>
this <is_it@valid.com>

Input (stdin)Download
9
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>

Expected Output
vineet <vineet@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>

'''

import email.utils
import re

for _ in range(int(input())):
    addr = email.utils.parseaddr(input())
    if re.match(r'[A-Za-z]+[\w\-.,]*@[A-Za-z]+\.[A-Za-z]{1,3}$', addr[1]):
        print(email.utils.formataddr(addr))
