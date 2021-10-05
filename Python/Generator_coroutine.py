

#############
# generator #
#############



def func():
    
    print('values:')
    for i in range(4):
        yield i # Like 'return' but does not return the value, that returns the Object Generator 


generaor = func()

print(generaor) # <generator object func at 0x7f85a9d1f9e0>

print(next(generaor)) # print('values:') & 1st value
print(next(generaor)) # 2nd value
print(next(generaor)) # 3rd value
print(next(generaor)) # 4th value

# print(next(generaor)) # We have error:StopIteration , becouse generator can itarate once

generaor = func()

for i in generaor: # becouse generator is iterable
    print(i)

# We use generators when the data array is required to save resources, 
# because the generator does not return value A returns the object 
# generator which with each iteration returns the value 
# Their main feature is to save the state between challenges. 

# EXAMPLE_1

def read_file_line_by_line(file_name): # Lazy reading file 
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line

f = read_file_line_by_line('python.zen')
print(type(f)) # <class 'generator'>
print(next(f),end='')
print(next(f),end='')
for line in f:
    print(line,end='')
print()

# EXAMPLE_2

gen = (x for x in range(2**2048))

print(next(gen))
print(next(gen))
for i in range(4):
    print(next(gen))

#############
# coroutine #
#############  

#      Generators return the data

#      Corutins consume data 

def print_line_contains(word):
    print("Searching for", word)
    while True:
        line = (yield)
        if word in line:
            print(line,end='')

search = print_line_contains('4')
print(type(search)) # <class 'generator'>
next(search) # init coroutine
search.send('1bn12') # send data to coroutine
search.send('564hj')
search.send('12356')
search.send('asd12')
search.close() # close coroutine
print()



# Realization 'grep' using 'generator' and 'coroutine' 


def grep(value,file): # search all lines contains 'value' in 'file'
    search = print_line_contains(value)
    next(search)
    for line in read_file_line_by_line(file):
        search.send(line)
    search.close()
    print('')


grep('better','python.zen') 