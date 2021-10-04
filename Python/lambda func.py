
def func():
    return True

def func_in_func(func):
    return func()


print(func_in_func(func) == func_in_func(lambda: True))
print(func_in_func(func))
print(func_in_func(lambda: True))
print(type(func_in_func))
print(type(lambda : True))



sentence =(
'''A list comprehension is a syntactic construct available 
in some programming languages for creating a list based 
on existing lists. It follows the form of the mathematical 
set-builder notation (set comprehension) as distinct from the  
use of map and filter functions. ''')

sentence2 = filter(lambda s: len(s) > 5, sentence.split())
print(' '.join(sentence2))







