def print_full_name(a, b):
    print(f'Hello {a} {b}! You just delved into python.')
    print(f"Hello {a} {b}! You just delved into python.")
    print('Hello {} {}! You just delved into python.'.format(a, b))
    print('Hello %s %s! You just delved into python.' % (a, b))
    return


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
