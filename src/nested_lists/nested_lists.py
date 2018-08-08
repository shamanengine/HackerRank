if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst.append((score, name))

    # print(lst)
    lst.sort()

    min = lst.pop(0)
    second_min_list = []

    for element in lst:
        if element[0] == min[0]:
            continue

        if not second_min_list:
            second_min_list.append(element)
        elif second_min_list[0][0] == element[0]:
            second_min_list.append(element)
        else:
            break

    print(second_min_list)

    for item in second_min_list:
        print(item[1])
