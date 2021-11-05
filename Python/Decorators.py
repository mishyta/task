from datetime import datetime


# def decorator(func):
#     def wrapper(*args, **kargs): # (*args, **kargs) if func get args
#         # what to do befor finc
#         func(*args, **kargs) 
#         # what to do after func
#         return # if func return somsing    
#     return wrapper


def get_func_execution_time(func):
    def wrapper(*args, **kargs):
        start = datetime.now()
        result = func(*args, **kargs)
        print(datetime.now() - start)
        return result

    return wrapper


@get_func_execution_time
def generate_list_1():
    return [i for i in range(2 ** 10) if i % 2 == 0]


@get_func_execution_time
def generate_list_2(n: int, d: int):
    return [i for i in range(n) if i % d == 0]


generate_list_1()
generate_list_2(2 ** 10, 7)


# Decorators like class

def print_call(method, class_name):
    def wrapper(*args, **kw):
        print(f'<object class="{class_name}"> call method: {method.__name__}({args},{kw})  ')
        result = method(*args, **kw)
        return result

    return wrapper


def MethodAnonser(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):

            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):

            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x

            attr = self._obj.__getattribute__(s)

            return print_call(attr, cls.__name__)

    return NewCls


@MethodAnonser
class Foo:
    def a(self, *args):
        pass

    def b(self, **kwargs):
        self.a(kwargs)


some_obbj = Foo()

some_obbj.a(1, 2, 2, 2, 2, 2, 2, 2)
some_obbj.b(name='Steve', surname='Cook')
