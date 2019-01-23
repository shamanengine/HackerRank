regex_pattern = r"M{,3}?" \
                 r"(CM)?((CD)?|(D?C{,3}?))?" \
                 r"(XC)?((XL)?|(L?X{,3}?))?" \
                 r"(IX)?((IV)?|(V?I{,3}?))?$"

import re

print(regex_pattern)

# print(str(bool(re.match(regex_pattern, input()))))

test_cases = {'I', 'II', 'III', }

tc_positive = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
               6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 19: 'XIX',
               20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 34: 'XXXIV', 39: 'XXXIX',
               60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
               200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
               2000: 'MM', 3000: 'MMM'}

tc_negative = {1: 'ac', 2: '2', 3: '$&^%', 4: 'IIV', 5: 'IIX',
               6: "XIIX", 7: "XIIV", 8: "ccX", 9: 'VIV', 10: 'LXL', 11: "IVV"}

# print("Test Cases:", "\t\t".join(map(str, tc_positive.keys())))

print("Positive:", end="\t")
for pk, pv in tc_positive.items():
    print(str(pk), ":", str(bool(re.match(regex_pattern, pv))), end='\t')

print("\nNegative:", end="\t")
for nk, nv in tc_negative.items():
    print(str(nk), ":", str(bool(re.match(regex_pattern, nv))), end='\t')


'''
Sample Input
CDXXI

Sample Output
True
'''