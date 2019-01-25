# 11
'''
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''

import re
from collections import OrderedDict

GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'


def validate_credit_card_number(credit_card_number: str) -> str:
    pattern1 = '^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    pattern2 = r'(?=^[456])' \
               r'(?=^[0-9]{16})'
    pattern3 = r'^.*(.).*\1{4}.*$'

    if re.search(pattern1, credit_card_number):
        credit_card_number = credit_card_number.replace("-", "")

    return "Valid" if re.search(pattern2, credit_card_number) \
                      and not re.search(pattern3, credit_card_number) else "Invalid"


test_cases = OrderedDict({
    '4123456789123456': 'Valid',
    '5123-4567-8912-3456': 'Valid',
    '61234-567-8912-3456': 'Invalid',
    '4123356789123456': 'Valid',
    '5133-3367-8912-3456': 'Invalid',
    '5123 - 3567 - 8912 - 3456': 'Invalid'})

for tck, tcv in test_cases.items():
    try:
        assert (validate_credit_card_number(tck) == tcv)
    except AssertionError:
        print(RED, "Failed:", tck, ":", tcv)
        continue
    print(GREEN, "Passed:", tck, ":", tcv)

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
