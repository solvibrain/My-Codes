# name=input("Enter the name")

# date=input("Enter the date")
# print('Dear,', name,

#   'you are selected!"you have to report at the following date', date)

name=input("Enter the name :  ")
date=input("Enter the date  :  ")

template='''Dear NAME 
                you are selected!
                DATE'''
print(template.replace("NAME",name).replace("DATE",date))                