'''
Input Format
The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Constraints
Each line is a non-empty string.

Output Format
Output a list containing the valid email addresses in lexicographical order.
If the list is empty, just output an empty list, [].
'''


def fun(s):
    # return True if s is a valid email, else return False
    return True if s else False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
'''
Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
