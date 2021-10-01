from random import choice
from string import ascii_uppercase, ascii_lowercase, digits
import string

 
def password_generator(length: int, from_what_generate = string.digits + string.ascii_lowercase + ascii_uppercase): 
    return (''.join(choice(from_what_generate) for i in range(length))) # use list comprehension to ganarate password

print(password_generator(5))

R = 100
DIVISIBLE_BY = 7

print('list of all odd numbers divisible by {}'.format(str(DIVISIBLE_BY)))

x1 = [i for i in range(R) if i % DIVISIBLE_BY == 0 and i % 2 != 0]
print(x1)


def sep_func(i):
    if i % DIVISIBLE_BY == 0 and i % 2 != 0:
        return i


x2 = [sep_func(i) for i in range(R)]
print(x2)

sentence =\
'''A list comprehension is a syntactic construct available 
in some programming languages for creating a list based 
on existing lists. It follows the form of the mathematical 
set-builder notation (set comprehension) as distinct from the  
use of map and filter functions. '''


def mark_vowels(letter):
    vowels = 'aeiou'
    if letter.isalpha() and letter.lower() in vowels:
        return '*'
    else:
        return letter


x3 = [mark_vowels(i) for i in sentence]
print(''.join(x3))



