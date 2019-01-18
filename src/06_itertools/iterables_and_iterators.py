import itertools

N, args, K = int(input()), input().split(), int(input())

tpls = list(itertools.combinations(args, K))

print(
    len(list(filter(lambda x: 'a' in x, tpls))) /
    len(tpls)
)

print(len([_ for _ in tpls if 'a' in _]) / len(tpls))
