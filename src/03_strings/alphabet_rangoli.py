def print_rangoli1(size):
    length = (size - 1) * 2 * 2 + 1

    for i in range(size * 2 - 1):
        print(chr(ord("a") + size - 1 - i).center(length, "-"))


def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    L = []

    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

------------------j------------------
"""