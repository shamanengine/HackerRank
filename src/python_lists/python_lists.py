if __name__ == '__main__':
    N = int(input())

    result_list = []
    for _ in range(N):
        command, *line = input().strip().lower().split()
        arguments = list(map(int, line))

        if "insert" == command:
            result_list.insert(arguments[0], arguments[1])
        elif "print" == command:
            print(result_list)
        elif "remove" == command and arguments[0] in result_list:
            result_list.remove(arguments[0])
        elif "append" == command:
            result_list.append(arguments[0])
        elif "sort" == command:
            result_list.sort()
        elif "pop" == command:
            result_list.pop()
        elif "reverse" == command:
            result_list.reverse()
        else:
            continue
