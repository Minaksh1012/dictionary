d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)


for x in d:
    x=int(input("enter the key"))
    if x in d:
        print("key is present in the dictionary ")
        break
    else :
        print("key is not present in dictionary")
        break    
