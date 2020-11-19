# 0 1 1 2 3 5 8 13 21 34

# with generators
def fibonaci_numbers(num):
    a = 0
    b = 1

    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


fib = fibonaci_numbers(20)

for i in fib:
    print(i)


# with a list
def fibonaci_numbers_list(num):
    a = 0
    b = 1
    fibonacci_list = []

    for i in range(num):
        fibonacci_list.append(a)
        temp = a
        a = b
        b = temp + b
    return fibonacci_list

print(fibonaci_numbers_list(20))