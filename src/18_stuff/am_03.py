'''

arr = input().strip().split()

# Python program to check if two strings are isomorphic
MAX_CHARS = 256


# This function returns true if str1 and str2 are isomorphic
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)

    # Length of both strings must be same for one to one
    # corresponance
    if m != n:
        return False

    # To mark visited characters in str2
    marked = [False] * MAX_CHARS

    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS

    # Process all characters one by one
    for i in range(n):

        # if current character of str1 is seen first
        # time in it.
        if map[ord(string1[i])] == -1:

            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])] == True:
                return False

            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True

            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]

            # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(string1[i])] != string2[i]:
            return False

    return True


print(areIsomorphic(arr[0], arr[1]))


/*
Words are considered isomorphic, if there is a reversible mapping (i.e. a bijection) between the letters of the source word and the letters of the target word.

e.g: "offer" is isomorphic to "apple" under o<->a, f<->p, e<->l, and r<->e

Given a collection of words, return them into groups where all the words in a group are isomorphic to each other

Example:

input:
"offer", "boo", "apple", "apply", "egg", "can"


output:
"offer", "apple", "apply"
"boo", "egg"
"can"

01123
offer

01123
apple

01023
opole


offerf

*/

def is_isomorphic(str1, str2):
    if (len(str1) != len(str2)):
        return False


def encode(input):
    hash_code = list()
    i = -1
    checked_letters = dict()
    for letter in input:
        if letter not in checked_letters.values():
            i += 1
            checked_letters[i] = letter
            hash_code.append(i)
        else:
            hash_code.append(list(checked_letters.keys())[list(checked_letters.values()).index(letter)]) # this should do the trick


    # print(checked_letters)

    return hash_code



'''




def encode(input):
    hash_code = list()
    i = -1
    checked_letters = dict()
    for letter in input:
        if letter not in checked_letters.values():
            i += 1
            checked_letters[i] = letter
            hash_code.append(i)
        else:
            hash_code.append(list(checked_letters.keys())[list(checked_letters.values()).index(letter)])

    print(checked_letters)

    return hash_code


print(encode("offerf"))
