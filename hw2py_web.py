class Meta:

    def __new__(cls, name, bases, attrs):
        count = Meta.children_number
        attrs['class_number'] = count 
        Meta.children_number += 1
        return type(name, bases, attrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

# print(Cls1.class_number)
# print(Cls2.class_number)
assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)