def func():
    return True

def func_in_func(func):
    return func()


print(func_in_func(func) == func_in_func(lambda: True))
print(func_in_func(func))
print(func_in_func(lambda: True))
print(type(func_in_func))
print(type(lambda : True))