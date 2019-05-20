'''
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
'''


def encode(input):
    hash_code = list()
    i = 0
    checked_letters = dict()
    for letter in input:
        if letter not in checked_letters.values():
            i += 1
            checked_letters[i] = letter
            hash_code.append(i)
        else:
            hash_code.append(list(checked_letters.keys())[list(checked_letters.values()).index(letter)])

    # print(checked_letters)

    return int("".join(map(str, hash_code)))


print(encode("offerf"))

if __name__ == '__main__':
    input = ["offer", "boo", "apple", "apply", "egg", "can"]

    groups = dict()
    print(encode(input[0]))
    groups[encode(input[0])] = {input[0]}
    print(groups)
    for word in input[1:]:
        hash_code = encode(word)
        if hash_code in groups.keys():
            groups[hash_code].add(word)
        else:
            groups[hash_code] = {word}

    print(groups)

"""
Example:
input:  "offer", "boo", "apple", "apply", "egg", "can"

output: 

"offer", "apple", "apply"
"boo", "egg"
"can"

"""
