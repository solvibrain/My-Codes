n1=int(input("Enter the number : "))
n2=int(input("Enter the number : "))
n3=int(input("Enter the number : "))

def great(a,b,c):
    if(a>b):
        if(a>c):
            print("a is greatest")
        else : 
            print("c is greatest")
    else :
        
        if(b>c):
            print("b is teh greatest number from the given nubmer .") 
        else: 
            print("c is the greatest number . ")    
great(n1,n2,n3)

