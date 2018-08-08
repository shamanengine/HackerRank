def minion_game(string):
    # Kevin has to make words starting with vowels.
    s_kevin = 0
    # Stuart has to make words starting with consonants.
    s_stuart = 0

    # Constants
    N = len(string)
    VOWELS = {"A", "E", "I", "O", "U"}

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

    for i in range(N):
        if s[i] in VOWELS:
            s_kevin += N - i
        else:
            s_stuart += N - i
        i += 1

    if s_kevin > s_stuart:
        print("Kevin", s_kevin)
    elif s_stuart > s_kevin:
        print("Stuart", s_stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
