#single element tuple can be created by using  , comma after the element  
# tuple can be created by using the tuple keyword list can also be convertd into tuple by using the tuple keyword
import imp


a=list(range(1,6))
b=tuple(a)
print(type(b))
# size of tuple is less than the list
import sys
my_list=a
my_tuple=b
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))
# time taken by machine to create a list is more than the tuple
# this can also be seen by using the timeit
import  timeit


a=list(range(1,6))
b=tuple(a)
my_list="[32,323,6,6,89]"
my_tuple="(3,6,9,0,)"
print(timeit.timeit(stmt=my_list, number=100000 )) 
print(timeit.timeit(stmt=my_tuple, number=100000 )) 

# Oner important point is checking that value is in the container or not 