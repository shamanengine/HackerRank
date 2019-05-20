class Polite:
    pass


obj1 = Polite()
obj1.attr = 10
print(obj1.attr)


class InPolite:
    def __setattr__(self, key, value):
        print('Not gonna set {}!'.format(key))


obj2 = InPolite()
obj2.attr = 10
print(obj2.attr)
