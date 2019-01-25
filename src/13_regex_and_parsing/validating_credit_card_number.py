'''
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''

import re


def validate_credit_card_number(credit_card_number: str) -> str:
    pattern1 = r'^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    pattern2 = r'(?=^[456])' \
               r'(?=^[0-9]{16})'
    pattern3 = r'^.*(.)\1{3}'

    if re.search(pattern1, credit_card_number):
        credit_card_number = credit_card_number.replace("-", "")

    return "Valid" if re.search(pattern2, credit_card_number) \
                      and not re.search(pattern3, credit_card_number) else "Invalid"


for _ in range(int(input())):
    print(_, validate_credit_card_number(input()))

from collections import OrderedDict

GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'

test_cases = OrderedDict({
    '4123456789123456': 'Valid',
    '5123-4567-8912-3456': 'Valid',
    '61234-567-8912-3456': 'Invalid',
    '4123356789123456': 'Valid',
    '5133-3367-8912-3456': 'Invalid',
    '5123 - 3567 - 8912 - 3456': 'Invalid',
    '6699889899699968': 'Valid'})

for tck, tcv in test_cases.items():
    try:
        assert (validate_credit_card_number(tck) == tcv)
    except AssertionError:
        print(RED, "Failed:", tck, ":", tcv)
        continue
    print(GREEN, "Passed:", tck, ":", tcv)

# print(bool(re.search(pattern1, "6699889899699968")))
# print(bool(re.search(pattern2, "6699889899699968")))
# print(bool(re.search(pattern3, "6699889899699968")))

'''
Sample Input
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output
Valid
Valid
Invalid
Valid
Invalid
Invalid
'''

'''
50
1182387522195848
4898285859544556
3533946521218854
2178579985193175
9691928949545344
1327576477684519
6885867822596993
1958129523778579
2357676157819124
9832746248713726
3673159777236652
8626186974574971
9687622296992497
6731749895254584
8231635922318254
7728878259735616
3347275338764373
6624557432269847
3164653818478977
7683817293887423
4654491168789767
6942469919536219
8434524674271379
6619249165433473
8842787232483367
5349898497837349
4841565975496529
7635659522159832
6699889899699968
5274676861386577
7261479482325831
9855821811363989
5462941623272486
2168457338741692
3493828267535654
7688277563695358
4621162653647299
5588937472734175
6313634439334582
2621731928824298
9356326214767474
6399396262113367
7326622854597675
2179646384144599
8723731421194264
9893925198222769
8493394862176119
9182146786584817
7865278423923993
5437343432579992

Invalid
Valid
Invalid
Invalid
Invalid
Invalid
Valid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Valid
Invalid
Invalid
Invalid
Valid
Invalid
Invalid
Valid
Valid
Invalid
Valid
Invalid
Valid
Valid
Invalid
Valid
Valid
Invalid
Invalid
Valid
Invalid
Invalid
Invalid
Valid
Valid
Valid
Invalid
Invalid
Valid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Valid
'''

'''
3
7635659522159832
6699889899699968
5274676861386577

Invalid
Valid
Valid
'''
