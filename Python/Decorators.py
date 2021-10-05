from datetime import datetime






# def decorator(func):
#     def wrapper(*args, **kargs): # (*args, **kargs) if func get args
#         # what todo befor finc
#         func(*args, **kargs) 
#         # what todo after func
#         return # if func return somsing    
#     return wrapper




def get_func_execution_time(func):
    def wrapper(*args,**kargs):
        start = datetime.now()
        result = func(*args,**kargs)
        print(datetime.now() - start)
        return result
    return wrapper


@get_func_execution_time
def generate_list_1():
    return [i for i in range(2**10) if i % 2 ==0]

@get_func_execution_time
def generate_list_2(n: int, d: int):
    return [i for i in range(n) if i % d == 0]


generate_list_1()
generate_list_2(2**10, 7)
