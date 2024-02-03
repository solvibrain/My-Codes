oxford={"chaku" : "Knife",
        "ravi" : "sunday",
         "tej" : "fast",
         "today" : "aaj",
         "tomorrow" : "kal",}
keys = input("Enter the word")

if(oxford.get(keys)==None) : 
    print("value not found")
else :   
    print("The value of the given word is : " , oxford.get(keys))