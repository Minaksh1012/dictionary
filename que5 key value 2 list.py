list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,] 

# Output :-

# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}




# res = {}
# for key in list1:
#     for value in list2:
#         res[key] = value
#         list2.remove(value)
#         break
# print(res)



f=0 
d={}
for i in list1:
    d[i]=list2[f]
    f+=1
print(d)    
