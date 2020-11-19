# def sum(n1, n2):
#     return n1 + n2
#
#
# print(sum(3, 4))


# docstrings

# def mul(n1, n2):
#     '''
#
#     :param n1:
#     :param n2:
#     :return: the multiplication
#     '''
#     return n1 * n2
#
#
# help(mul)


# *args, **kwargs

def sumatoria(*args):
    return sum(args)

suma = sumatoria(1, 2, 3, 4)

print(suma)
