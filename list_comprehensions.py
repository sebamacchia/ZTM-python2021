# list comprehension

list1 = [num for num in range(100) if num % 2 == 0]
print(list1)

my_dict = {k: k * 2 for k in [1, 2, 3]}
print(my_dict)

some_list = ['a', 'b', 'c', 'a', 'f', 'c']

duplicates = [item for item in set(some_list)]

print(duplicates)
