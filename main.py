class SomeClass(object):
    attr = 41

    def method_1(self, x: int):
        print(2 * x)

obj = SomeClass()
obj.method_1(6)
print(obj.attr)