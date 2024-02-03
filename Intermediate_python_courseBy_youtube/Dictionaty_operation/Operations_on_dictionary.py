# in Dictionary there is key and value pair 
# if original dictionary is assigned to copyied one and if we modified the copyied one than the original one also get chaged.
# update mehtod is to update the previous dictionary 
my_dict={"name":"Rupesh","age":32,"email":"xyz@gmail.com"}
my_dict1=dict(name="Rupan",age=34, email="aaad@gmail.com",city="Hongkong")
my_dict.update(my_dict1)# through this we can update the dictionary in a practical use.
print(my_dict1)
# LIst is not accepatable as a key in dictionaty 
# but tuple is accepated as key in dictionary 