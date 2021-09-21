# Write a program to print 'exists' if entered key already exists in the 
# dictionary and print 'not exists' if the entered key does not exist.
# Example :-

dict={"name":"Raju", "marks":56}

# if input is “name” then output will be “exist”

# If input is “class” then output will be “not exists”.

s=input("enter the key name : ")
if s in dict:
    print("exist")
else:
    print("Not exist")   