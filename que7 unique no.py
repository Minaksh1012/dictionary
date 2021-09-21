#  [

#      {"first":"1"}, 

#      {"second": "2"}, 

#      {"third": "1"}, 

#      {"four": "5"}, 

#      {"five":"5"}, 

#      {"six":"9"},

#      {"seven":"7"}

# ]

# Output :-

# [2', '7', '9', '5', '1'] 

 

list1=[ {"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}

]
# b=[]
# dic1=list (list1)
# for v in dic1:
#      if v not in dic1[v]:
#           b.append(v)
# print(b)
list3=[]
list2=list(list1)
for v in list2:
     print(v)
     for j in not list3:
          j.append(list3)
     print(list3)




# for i in list1:
#     if i not in list1[i]:
#         list1.append(i)
#         list1.sort()
# print(list1)

