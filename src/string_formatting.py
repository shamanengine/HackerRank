#
# print('{:x}'.format(1))
#
# "{0:d} {0:x} {0:o} {0:b}".format(i)

def print_formatted(number):
    # your code goes here
    result = ""
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        result += "{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}\n".format(i, width=width).upper()
    print(result)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
