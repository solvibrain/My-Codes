m1 = int(input("Enter the marks in Subject 1 : "))
m2 = int(input("Enter the marks in Subject 2 : "))
m3 = int(input("Enter the marks in Subject 3 : "))

perc = (m1+m2+m3)/3

if(perc>40):

    if(m1<33 or m2<33 or m3<33) :
        print("you fail the examination becausee your score in one subject is less than the minimum marks")
    else :
        print("you have passed the examination. All the best for the future.")    
    

else :
    print("you fail the Examination. But you can try next time.")    