# marks1 = int(input("Enter the marks1 : " ))
# marks2 = int(input("Enter the marks2 : " ))
# marks3 = int(input("Enter the marks3 : " ))
# marks4 = int(input("Enter the marks4 : " ))
# marks5 = int(input("Enter the marks5 : " ))
# marks6 = int(input("Enter the marks6 : " ))

# listOfMarks = [marks1,marks2,marks3,marks4,marks5,marks6]
# listOfMarks.sort()
# print(listOfMarks)
# l=[]
# for i in range(5):
#     i= input("Enter the name of the fruits : ")
#     l.append(i)

# print(l)


l=[]
for i in range(10 ):
    i= int(input("Enter the Marks of the Students   : "))
    l.append(i)
    
print(l)
l.sort()
print(l)

#suming the elements in the list 
sum=0
for i in range(len(l)):
     
     sum=sum+l[i]

print(sum)