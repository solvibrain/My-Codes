my_set=set("Rupesh")# this is also the unique to know the number of unique letter in any sentence or word.
print(my_set)
# for defining the empty set we should use set() not {}
my_set=set()# this having the type set 
my_set1={} # whereas this having the type dictionary

print(type(my_set))
print(type(my_set1))

# ther is add() for addng elements  in the set
# remove() is to remove the element if the element is not present in the set than is going to give error while 
# using of discard() does not give any type of error 
# # .pop() will remove any arbitary value from the set 
# frozen set is unmutable .
set1=frozenset(list(range(1,6)))
set1.add(6)
print(set1)