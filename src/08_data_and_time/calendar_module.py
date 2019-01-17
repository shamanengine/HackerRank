import calendar

# print(eval('list(calendar.day_name)[calendar.weekday({2},{0},{1})].upper()'.format(*list(map(int, input().split())))))
# print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

'''
Sample Input
08 05 2015

Sample Output
WEDNESDAY
'''