some_list = ['a', 'b', 'c', 'a','h','h']

duplicates =[]
for i in some_list:
    if i not in duplicates:
        duplicates.append(i)
    else:
        print(i)

