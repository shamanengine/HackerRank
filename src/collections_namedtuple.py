from collections import namedtuple

N, Sheet = int(input()), namedtuple('Sheet', input().strip().split())
print('%.2f' % (sum([int(Sheet._make(input().strip().split()).MARKS) for _ in range(N)]) / N))
