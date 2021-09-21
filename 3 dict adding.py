# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

for key in dic1:
    if key in dic2:
        dic2.update(dic1)
    else:
        dic2[key]=dic1[key]    
print(dic2)    



# for i in dic1:
#     if i in dic2:
#         dic2.update(dic3)
# print(dic2)        