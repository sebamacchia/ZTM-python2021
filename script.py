# Fundamental data types
# int
n = 3 * 7
print(n)
print(type(n))

# float
f = 5.6
print(f)
print(type(f))

# bool

is_cool = True
has_money = False

# str
name = 'seba'
last_name = 'macc'
# string conctention
print('hola'+str(100))
full_name = name

#Formated strings
print(f'hola {name}')

# list
li = [1,2,3,4]
li2 = [1,'a', True]
#matrix, is a multidimentional list
matrix = [
    [1,2,3],
    [4,5,6]
]
#list unpacking
a,b,*other,c = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(other)
print(c)

# tuple
# are inmutable
my_tuple = (1,2,3,4)

# set


# dictionary
# dic
# data structure
dictionary = {
    'a':1,
    'b':2,
    1: 'la_chota'
}
print('dict: ',dictionary[1])
#dictionary keys have to be inmutable
print('get: ',dictionary.get('i'))


# Math Functions:
n = round(3.4)
print(n)

# Varibles

a,b,c = 1,2,3
print('a:', a,'/', 'b:', b)

# Expresion vs staiments

n = 10
b = n-1 #n-1 is an expresion, an staiment is all the line, o sea, b = n-1

#methods
#for example strings has his methods
quote ='to be or not to be'
print(quote.upper())

# Classes -> custom types

# Specialized data types
# Modules

#None
#absence of value