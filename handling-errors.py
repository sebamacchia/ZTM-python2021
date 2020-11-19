# Handling Errors

while True:
    try:
        age = int(input("enter your age?"))
        10/age
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('not a zero')
    else:
        print(f'thanks, you are {age} yos')
        break
