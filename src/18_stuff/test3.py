# print(ord("A"))

# for c in [a-z]:

print([chr(i) for i in range(ord('A'), ord('z') + 1)])

for c in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
    C = chr(ord(c) + ord("a") - ord("A"))
    print(c, "\t", ord(c), "\t", C, "\t", ord(C), "\t")

number = 111
print("".join(chr(number) if number // (ord("z") + 1) == 0 else chr(ord("a") + number % (ord("z") + 1))))

# A - 65
# Z - 90
# a - 97
# z - 122

# print(87 // 90)
