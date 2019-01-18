def wrap(string, max_width):
    result = ""
    for _ in range(0, len(string), max_width):
        result += string[_:_ + max_width] + "\n"
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
