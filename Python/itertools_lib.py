

from itertools import *


# The ITERTOOLS module is a collection of useful iterators. 

# itertools iterators:
#
# 'accumulate' 
# 'chain'
# 'combinations'
# 'combinations_with_replacement' 
# 'compress' 
# 'count' 
# 'cycle' 
# 'dropwhile' 
# 'filterfalse'
# 'groupby' 
# 'islice' 
# 'permutations' 
# 'product'
# 'repeat'
# 'starmap'
# 'takewhile'
# 'tee'
# 'zip_longest'
#

data1 = 'ABC'
data2 = [1,2,3]

# Infinite iteration
#  
# count(start, step)
# cycle(iterable_object)
# repeat(element, times)

count(0, 3) # 0 3 6 9...
cycle(data2) # 1 2 3 1 2 3 1 ....
repeat(data1, 3) # ABC ABC ABC

# Combinatoric iterators:
#
# product(iteerable_object, repeat = n )
# permutations(iterable_object, r=None)
# combinations()
# combinations_with_replacement()
#

# product = Cartesovo Product Items Items 

itertools_object = product(data1,repeat = 2) # -> <itertools.accumulate object at ...>
print(list(itertools_object)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

itertools_object = product(data2,repeat = 3) 
print(list(itertools_object))                # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), 
                                             # (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3), 
                                             # (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3)]

print(list(itertools_object)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# permutations = r-length tuples, all possible orderings, no repeated elements

itertools_object = permutations(data1)
print(list(itertools_object)) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# End iterators: 
#
# All that remain 
#


# accumulate = value[0], value[0]+value[1], ..., value[0]+value[1]+...+value[n]

itertools_object = accumulate(data1) # -> <itertools.accumulate object at ...>
print(list(itertools_object)) # ['A', 'AB', 'ABC']

itertools_object = accumulate(data2) 
print(list(itertools_object)) # [1, 3, 6]


#
# In the module there are many different interesting iterators, I reviewed the douchilla for example.
#
#

from os import times
import time



def loading_line(times:int = 3, speed:float = 0.1, value:str = 'loading...') -> None:
    for i in range(0,times):
        for n in accumulate(value):
            print(n)
            time.sleep(speed)
            print("\033[A                             \033[A")

# groupby
data = 'Make an iterator that returns consecutive keys and groups from the iterable.'

# count the number of repetitions of characters
def count_symbols(data) -> dict:
    # returns dict where key=symbol value=number of repetitions
    data = sorted(data.lower())
    return {k:len(list(g)) for k, g in groupby(data)}

print(count_symbols(data))