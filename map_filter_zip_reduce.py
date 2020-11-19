# map()

# help(map)


def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def multiply_by_2map(item):
    return item * 2


print(list(map(multiply_by_2map, [1, 2, 3])))

# filer()

my_list = [1, 2, 3, 4]


def check_odd(item):
    return item % 2 != 0


odd_list = list(filter(check_odd, my_list))
print(odd_list)

# zip
your_list = [10, 20, 30, 40]
zipeado = list(zip(my_list, your_list))
print(zipeado)

# reduce
from functools import reduce

help(reduce)
acumulator = reduce(lambda x, y: x + y, [1, 2, 3])
print(acumulator)
