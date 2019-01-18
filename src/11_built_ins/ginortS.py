s = input()
print("".join(sorted(filter(lambda x: x.isalpha() and x.islower(), s)) +
              sorted(filter(lambda x: x.isalpha() and x.isupper(), s)) +
              sorted(filter(lambda x: x.isdigit() and not int(x) % 2 == 0, s)) +
              sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 0, s))))
