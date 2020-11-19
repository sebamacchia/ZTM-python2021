# parameters

def say_hello(name, emoji):
    print(f'hi {name} you are a {emoji}')

# positional arguments
say_hello('seba', '😀')
say_hello('caca', '😀')

# keyword arguments
say_hello(emoji='😀', name='seba')

# default paramenters
def say_hello2(name='Bart', emoji='G'):
    print(f'hi {name} you are a {emoji}')

say_hello2('seba')