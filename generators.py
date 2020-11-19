# We have a list, that take a place in the memory
# a list is iterable:

def list_maker(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = list_maker(100)
print('list: ', my_list)
print('~~~~~~~~~~~~~~~~~~~')


# that take a big space in memory

def genetaror_func(num):
    for i in range(num):
        yield i * 2


a = genetaror_func(100)
print(a)
print('primer item: ', next(a))
print('second item: ', next(a))

# we handle just one item in memory
for item in a:
    print(item)

print('##########################')


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


print('##########################')

special_for([1, 2, 3])

# so range() is a generator, we will create our own range:

print("RANGEEEEEEEEE")


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.fist = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
