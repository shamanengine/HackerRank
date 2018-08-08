def count_substring(string, sub_string):
    start = count = 0

    while True:
        start = string.find(sub_string, start)
        if start != -1:
            count += 1
            start += 1
        else:
            break

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
