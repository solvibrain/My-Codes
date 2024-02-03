list=["Rupesh","Ritesh", "Sonam","Rupam"]
list1=list.reverse() # this methos is used for the reversing the list. 
list.sort()# this is the one way to sort the list.
list1=sorted(list)# this is also the way to sort the list myy taking the new list variable
print(list1)
#printing same number as many time is 
mylist=[3]*12
print(mylist)
#concatenation 
#Slicing
#The simplest method to reverse any list is using the slicing
list2=[3,5,6,3,7,8,0]
list3=list2[::-1]# slicing take the new list
print(list3)

#When we assign one list to another list there are soem ambiguity
word="Soving Problem by a unique wqay "
list_org=word.split()
list_new=list_org
list_new.append("Rupesh")# HEre we modified the new list and the original also get chages
print(list_org)# here is the ambiguity that we are modifying the new list and the original one also get changes
                # to prevent this we simply use copy() method
list_new=list_org.copy()# there are some other method also 
list_new=list(list_org)# this is the one way and the other is way by slicing 

list_new.append("Ritesh")
print(list_org)                
# other simple way to create the new list is by list comprehension
