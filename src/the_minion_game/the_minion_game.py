def minion_game(string):
    # your code goes here
    # string = string.strip().upper()
    # Kevin has to make words starting with vowels.
    Kevin = {}
    # Stuart has to make words starting with consonants.
    Stuart = {}
    i = 0

    # ABA

    # Kevin
    # A     2
    # AB    1
    # ABA   1
    # Total 4

    # Stuart
    # B     1
    # BA    1
    # Total 2

    for s in string:
        if s in ["A", "E", "I", "O", "U"]:
            for j in range(len(string) - i):
                add_string(Kevin, string[i:i + j + 1])
        else:
            for j in range(len(string) - i):
                add_string(Stuart, string[i:i + j + 1])
        i += 1

    # print("==Kevin== \n", Kevin)
    # print("==Stuart== \n", Stuart)
    # print("Kevin", sum(Kevin.values()))
    # print("Stuart", sum(Stuart.values()))

    s_kevin = sum(Kevin.values())
    s_stuart = sum(Stuart.values())

    if s_kevin > s_stuart:
        print("Kevin", s_kevin)
    elif s_stuart > s_kevin:
        print("Stuart", s_stuart)
    else:
        print("Draw")


def add_string(score_dict, s):
    if s in score_dict.keys():
        score_dict[s] += 1
    else:
        score_dict[s] = 1


if __name__ == '__main__':
    s = input()
    minion_game(s)
