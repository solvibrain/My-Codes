def sumofnaturalnum(n):
    # a=(n*(n+1))/2 #this is being solved by usig the formula .d
    # return a
    sum=0
    for i in range(1,n+1):#This can be done by iteration . 
        sum+=i
    print("Sum of the nTH natural number is ",sum)    

c=int(input("Enter the number : "))
sumofnaturalnum(c)    
