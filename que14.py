my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
# expect result:-['e','b','c']



a=[]
for i in my_dict:
    a.append(my_dict[i])
p=sorted(a)
u=[]
y=1
while y<=3:
    u.append(p[-y])
    y+=1
print(u)          



    











# # for x in my_dict:
# #     print(x)

    










