lst_num1 = [1, 2, 3.0004]


def func(lst_num):
    return list(map(str, lst_num))


a = func(lst_num1)

b = list(map(lambda x: str(x), lst_num1))

print(a, b, sep="\n")
